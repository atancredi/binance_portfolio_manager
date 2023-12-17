from typing import List, Optional
from datetime import datetime
import pytz

from binance.client import Client
from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_MARKET

from account import Account
from orders import Orders
from trades import Trades
from constants import CoinPair
from portfolio import Portfolio
from data import TradeData

from config import read_config

from tinydb import TinyDB
from json import dumps

class BinanceApi:
    def __init__(self, config_name = "config"):
        config = read_config(config_path = config_name)
        self.__client = Client(config["API_KEY"], config["API_SECRET"])
        self.orders = Orders(self.__client)
        self.account = Account(self.__client)
        self.trades = Trades(self.__client)
    
    def get_orders(self, symbol: CoinPair):
        return self.__client.get_all_orders(symbol=symbol)

    def get_prices(self, symbols: List[CoinPair]) -> dict:
        _symbols = [symbol.value for symbol in symbols]
        prices = self.__client.get_all_tickers()
        return {price['symbol']: price['price'] for price in prices if price['symbol'] in _symbols}
    
    def buy_portfolio(self, qty: float, portfolio: dict, db: Optional[TinyDB] = None):
        orders = []
        for pair in portfolio:

            #First get price
            price = self.__client.get_symbol_ticker(symbol=pair+"USDT")
            info = self.__client.get_symbol_info(symbol=pair+"USDT")
            min_notional = float(info['filters'][6]["minNotional"])
            step_size = float(info['filters'][1]["stepSize"])
            decimals = 0 if str(step_size).split('.')[0] == '1' else len(str(step_size).split('.')[1])
            min_qty = float(info['filters'][1]["minQty"])

            # Calculate how much
            print(f"{pair}: {portfolio[pair]}%")
            allocated_usdt = qty / 100 * portfolio[pair]
            print(f"Allocated {allocated_usdt} USDT")
            needed_quantity = round(allocated_usdt / float(price['price']),decimals)
            print(f"Need to have {needed_quantity} {pair}")

            # How much do i have?
            account_balance = float(self.account.get_coin_balance(pair)["free"])
            print(f"Already have {account_balance} {pair}")
            
            # How much do i have to buy?
            buy_quantity = needed_quantity - account_balance
            print(f"Need too buy {buy_quantity} {pair}")

            if buy_quantity < float(info['filters'][1]["minQty"]):
                print(f"Need to buy at least {info['filters'][1]['minQty']} {pair}")
                print("\n")
                continue
            
            # print((buy_quantity - min_qty) % step_size)
            if (buy_quantity - min_qty) % step_size > min_qty:
                print(f"Buy quantity must be multiple of {step_size} {pair}")
                print("\n")
                continue

            if buy_quantity * float(price['price']) < min_notional:
                print(f"Notional order value must be at least {min_notional} {pair}")
                print("\n")
                continue
                
            print("\n")

            # Add order to list
            order = {
                "symbol": pair+"USDT",
                "quantity": buy_quantity
            }
            orders.append(order)
                    
        print(dumps(orders, indent=4))
        if input("Abort? press x \n") == "x":
            print("exiting")
            exit()
        
        print("Executing")
        
        # review orders
        for order in orders:

            print(f"Buying {order['quantity']} {order['symbol']}")

            # Buy
            res = self.__client.order_market_buy(
                symbol=order["symbol"],
                quantity=order["quantity"]
            )
            print(res)

            # Add to DB
            ts = datetime.now(pytz.timezone("Europe/Berlin")).isoformat(timespec="seconds").replace("+01:00","Z")
            for fill in res["fills"]:
                d = TradeData(pair=order["symbol"], quantity=order["quantity"], price=fill["price"], order_type="buy", timestamp=ts)
                db.insert(d.__dict__)
