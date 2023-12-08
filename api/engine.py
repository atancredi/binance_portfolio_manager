from binance.client import Client

from account import Account
from orders import Orders
from trades import Trades

from config import read_config

class BinanceApi:
    def __init__(self):
        config = read_config()
        self.__client = Client(config["API_KEY"], config["API_SECRET"])
        self.orders = Orders(self.__client)
        self.account = Account(self.__client)
        self.trades = Trades(self.__client)
