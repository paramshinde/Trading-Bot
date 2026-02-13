from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger()

class OrderService:
    def __init__(self):
        self.client = BinanceClient()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity
            }

            if order_type == "STOP":
                params["type"] = "STOP_MARKET"
                params["stopPrice"] = price


            logger.info(f"Request: {params}")

            response = self.client.create_order(**params)

            logger.info(f"Response: {response}")

            return response

        except Exception as e:
            logger.error(f"Error placing order: {str(e)}")
            print(f"FULL ERROR: {repr(e)}")  # 👈 add this
            raise
    def get_order_status(self, symbol, order_id):
        return self.client.get_order(symbol, order_id)


