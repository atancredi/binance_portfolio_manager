from tinydb import TinyDB
from data import TradeData
from constants import CoinPair


from json import dumps
td = TinyDB("trades.json")

# print(dumps(td.all(), indent=4))

data = TradeData(
    pair=CoinPair.ROSEUSDT,
    quantity=61.8,
    price=0.08635,
    timestamp="2023-12-09T02:54:48Z",
    order_type= "sell"
)

td.insert(data.__dict__)