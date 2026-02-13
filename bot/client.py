from binance.client import Client
from config import API_KEY, API_SECRET

class BinanceClient:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)

        #  THIS IS REQUIRED FOR TESTNET
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def create_order(self, **params):
        return self.client.futures_create_order(**params)

    def get_order(self, symbol, order_id):
        return self.client.futures_get_order(symbol=symbol, orderId=order_id)

