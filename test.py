from api import BinanceApi
from constants import CoinPairs


if __name__ == '__main__':
    my_api = BinanceApi()
    account_details = my_api.account.get_account()
    # print('Account: ', account_details)
    print('Spot Balance: ', my_api.account.get_spot_balance())
    # orders = my_api.orders.get_buy_orders(CoinPairs.BNBUSDT)
    # print(orders)
    my_api.orders.get_all_orders(CoinPairs.BTCUSDT, pretty_print=True)
    # average_price = my_api.orders.get_avg_buy_price(CoinPairs.BTCUSDT)
    # print(average_price)
    # print(my_api.trades.get_trades(CoinPairs.ETHUSDT))
    # print(my_api.trades.get_total_commission_paid(CoinPairs.ETHUSDT))
