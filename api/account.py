
from binance import Client


class Account:
    def __init__(self, client: Client):
        self.__client = client

    def get_account(self):
        return self.__client.get_account()

    def get_spot_balance(self):
        spot_balance_list = []
        details = self.__client.get_account()

        if details['accountType'] == 'SPOT':
            spot_balance_list = [{item['asset']: {'total': (float(item['free']) + float(item['locked'])),
                                                  'free': item['free'], 'locked': item['locked']}}
                                 for item in details['balances'] if (float(item['free']) + float(item['locked'])) > 0]

        return spot_balance_list
