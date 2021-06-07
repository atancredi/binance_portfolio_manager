from binance import Client


class Trades:
    def __init__(self, client: Client):
        self.__client = client

    def get_trades(self, symbol):
        return self.__client.get_my_trades(symbol=symbol)

    def get_total_commission_paid(self, symbol, commission_asset='BNB'):
        return sum([float(trade['commission']) for trade in self.get_trades(symbol=symbol) if trade[
            'commissionAsset'] == commission_asset])
