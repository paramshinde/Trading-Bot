import click
from bot.orders import OrderService
from bot.validators import *

@click.command()
@click.option('--symbol', required=True, help="Trading pair (e.g., BTCUSDT)")
@click.option('--side', required=True, help="BUY or SELL")
@click.option('--order_type', required=True, help="MARKET or LIMIT")
@click.option('--quantity', required=True, type=float)
@click.option('--price', type=float, default=None)

def main(symbol, side, order_type, quantity, price):
    try:
        # Validation
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        service = OrderService()

        print("\n Order Request")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")

        response = service.place_order(
            symbol, side, order_type, quantity, price
        )

        print("\n Order Placed Successfully!")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        status = service.get_order_status(symbol, response.get("orderId"))
        print("\n Updated Order Status:")
        print(f"Status: {status.get('status')}")
        print(f"Executed Qty: {status.get('executedQty')}")
        print(f"Avg Price: {status.get('avgPrice')}")

    except Exception as e:
        print(f"\n Error: {str(e)}")

if __name__ == "__main__":
    main()
