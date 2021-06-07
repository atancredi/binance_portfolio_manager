from binance import Client


class Orders:
    def __init__(self, client: Client):
        self.__client = client

    def get_all_orders(self, symbol, view_filled_only=True, pretty_print=False):
        orders = self.__client.get_all_orders(symbol=symbol)
        if view_filled_only:
            orders = [order for order in orders if order['status'] == 'FILLED']

        if pretty_print:
            for i, order in enumerate(orders):
                print(f'Order {i+1}: {order}')

        return orders

    def get_buy_orders(self, symbol):
        return [order for order in self.get_all_orders(symbol=symbol, view_filled_only=True)
                if order['side'] == 'BUY']

    def get_sell_orders(self, symbol):
        return [order for order in self.get_all_orders(symbol=symbol, view_filled_only=True)
                if order['side'] == 'SELL']

    def get_avg_buy_price(self, symbol):
        buy_orders = self.get_buy_orders(symbol=symbol)
        return sum([float(order['price']) for order in buy_orders])/len(buy_orders)
