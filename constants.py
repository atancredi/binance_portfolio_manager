from enum import Enum
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

SECRET_FILE_PATH = f'{PROJECT_ROOT}/secret'


class CoinPairs(str, Enum):
    BNBUSDT = 'BNBUSDT'
    ETHUSDT = 'ETHUSDT'
    BTCUSDT = 'BTCUSDT'
    ETHEUR = 'ETHEUR'
    BTCEUR = 'BTCEUR'
    WRXUSDT = 'WRXUSDT'

    def __str__(self):
        return str(self.value)
