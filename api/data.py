from constants import CoinPair

class TradeData:
    pair: CoinPair
    quantity: float
    price: float
    timestamp: str
    order_type: str

    def __init__(self, pair: CoinPair, quantity: float, price: float, order_type: str, timestamp: str):
        self.pair = pair
        self.quantity = quantity
        self.price = price
        self.timestamp = timestamp
        self.order_type = order_type