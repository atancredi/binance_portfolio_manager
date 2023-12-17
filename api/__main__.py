from dateutil.parser import isoparse
from json import dumps

from engine import BinanceApi
from constants import CoinPair
from portfolio import Portfolio

from tinydb import TinyDB, Query


if __name__ == '__main__':
    api = BinanceApi("config_trade")

    # a = api.get_orders(CoinPair.SOLUSDT)
    # print(a)

    rebalancing = {
        "AGIX": 50,
        "FET": 30,
        "NMR": 10,
        "MDT": 10
    }

    api.buy_portfolio(51, rebalancing, TinyDB("rebalancing_order.json"))