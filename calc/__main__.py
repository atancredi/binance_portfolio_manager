from datetime import datetime
from json import dumps

from binance.client import Client

from config import read_config

config = read_config("config_view")
client = Client(config['API_KEY'], config['API_SECRET'])

all_tickers = {}
for ticker in client.get_all_tickers():
    all_tickers[ticker["symbol"]] = ticker["price"]

# Binance object is created
ignore_coins = ["EASY","LDAXS","BNB"]
balances = []
for balance in client.get_account()['balances']:
    if balance["asset"] in ignore_coins:
        continue
    free = float(balance['free'])
    locked = float(balance['locked'])
    if free > 0 or locked > 0:
        data = {
            'asset' : balance['asset'],
            'free' : free,
            'locked' : locked
        }
        if balance['asset'] != 'USDT':
            data["free_value_usdt"] = free * float(all_tickers[balance['asset'] + 'USDT'])
        balances.append(data)

assets_data = []
for asset in balances:
    if asset["asset"] == "USDT":
        continue
    # print(asset)
    asset_orders = []
    asset_usdt_balance = 0
    for order in client.get_all_orders(symbol = asset["asset"]+"USDT"):
        if order["status"] == "FILLED":

            date = datetime.fromtimestamp(order["time"] / 1000)
            if date.year < 2023:
                continue
            
            amount = float(order["cummulativeQuoteQty"])
            if order["side"] == "BUY":
                amount = amount * -1
            
            filled = float(order["executedQty"])
            if order["side"] == "SELL":
                filled = filled * -1
            
            # TODO Any info about the price? 

            asset_usdt_balance += amount
            asset_orders.append({
                "amount": amount,
                "filled": filled,
                "date": date.isoformat()
            })
    assets_data.append({
        "asset" : asset["asset"],
        "free" : asset["free"],
        "locked" : asset["locked"],
        "orders" : asset_orders,
        "total_orders_balance_usdt": asset_usdt_balance,
        "free_value_usdt" : asset["free_value_usdt"],
        "total_orders_value_usdt" : asset_usdt_balance + asset["free_value_usdt"]
    })

    # TODO make this into an api

print(dumps(sorted(assets_data, key=lambda x: x["total_orders_value_usdt"], reverse=True),indent=4))