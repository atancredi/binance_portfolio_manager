from enum import Enum

class CoinPair(str, Enum):
    BNBUSDT = 'BNBUSDT'
    ETHUSDT = 'ETHUSDT'
    BTCUSDT = 'BTCUSDT'
    ADAUSDT = 'ADAUSDT'
    FETUSDT = 'FETUSDT'
    MATICUSDT = 'MATICUSDT'
    SOLUSDT = 'SOLUSDT'
    SOLBNB = 'SOLBNB'
    DOTUSDT = 'DOTUSDT'
    INJUSDT = 'INJUSDT'
    ROSEUSDT = 'ROSEUSDT'
    GRTUSDT = 'GRTUSDT'
    AGIXUSDT = 'AGIXUSDT'
    AXSUSDT = 'AXSUSDT'
    RNDRUSDT = 'RNDRUSDT'

    def __str__(self):
        return str(self.value)
