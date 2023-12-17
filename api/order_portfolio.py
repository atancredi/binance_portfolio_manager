from dateutil.parser import isoparse
from json import dumps

from engine import BinanceApi
from constants import CoinPair
from portfolio import Portfolio

from tinydb import TinyDB, Query


if __name__ == '__main__':
    my_api = BinanceApi()
    # account_details = my_api.account.get_account()
    # print('Account: ', account_details)

    portfolio = Portfolio()
    portfolio.defined_pairs = [
        CoinPair.SOLUSDT,
        CoinPair.ROSEUSDT,
        CoinPair.ADAUSDT,
        CoinPair.INJUSDT,
        CoinPair.RNDRUSDT,
        CoinPair.DOTUSDT,
        CoinPair.GRTUSDT,
        CoinPair.MATICUSDT,
        CoinPair.FETUSDT,
        CoinPair.AGIXUSDT
    ]

    trades = TinyDB("trades.json")
    # my_api.buy_portfolio(10, portfolio, trades)

    print(dumps(trades.all(),indent=4))

    # prices = my_api.get_prices(portfolio.defined_pairs)

    # for pair in portfolio.defined_pairs:
    #     current_price = prices[pair.value]
    #     print(f"current price: {current_price}")

    #     r = sorted(trades.search(Query().symbol == str(pair)), key=lambda x: isoparse(x['timestamp']))

    #     for trade in r:
    #         print(trade)
        
    #     print("\n")
