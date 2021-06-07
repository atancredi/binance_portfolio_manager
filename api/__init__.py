import os
from configparser import ConfigParser

from binance import Client

from api.account import Account
from api.orders import Orders
from api.trades import Trades
from custome_exceptions import ConfigurationError
from constants import SECRET_FILE_PATH

__API_KEY__ = __API_SECRET__ = None


def read_secrets():
    global __API_SECRET__, __API_KEY__
    print('Checking secret file for secret')
    try:
        config = ConfigParser()
        config.read(SECRET_FILE_PATH)
        __API_KEY__ = config['SECRET']['API_KEY']
        __API_SECRET__ = config['SECRET']['API_SECRET']

    except Exception as e:
        print('Error occured while reading secret from file.')

    if not __API_KEY__ or not __API_SECRET__:
        print('Checking environment variables for secret')
        try:
            __API_KEY__ = os.environ['API_KEY']
            __API_SECRET__ = os.environ['API_SECRET']
        except KeyError as ke:
            print('Error occurred while reading secret from environment variables')

    if not __API_KEY__ or not __API_SECRET__:
        raise ConfigurationError('No secret found')


class BinanceApi:
    def __init__(self):
        read_secrets()
        self.__client = Client(__API_KEY__, __API_SECRET__)
        self.orders = Orders(self.__client)
        self.account = Account(self.__client)
        self.trades = Trades(self.__client)
