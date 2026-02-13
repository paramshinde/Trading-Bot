# # Binance Futures Testnet Trading Bot

A Python-based CLI trading bot that interacts with the Binance Futures Testnet (USDT-M) to place MARKET, LIMIT, and STOP orders.

This project demonstrates API integration, structured code design, input validation, logging, and error handling.

---

##  Features

- Place **MARKET**, **LIMIT**, and **STOP** orders
- Supports both **BUY** and **SELL**
- CLI-based interface using Click
- Input validation for all parameters
- Logging of API requests, responses, and errors
- Structured and reusable codebase
- Error handling for API and network failures

---

##  Tech Stack

- Python 3.x
- python-binance
- Click (CLI)
- python-dotenv
- Logging module

---

##  Setup Instructions

###  Clone the Repository

bash
git clone https://github.com/your-username/binance-futures-trading-bot.git
cd binance-futures-trading-bot

## Install Dependencies
pip install -r requirements.txt

## Create .env File
BINANCE_API_KEY=your_api_key

BINANCE_API_SECRET=your_api_secret

Use Binance Futures Testnet API keys

## Testnet URL
https://testnet.binancefuture.com

## Run the Application
Use the CLI commands below.

1.Market Order

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.002

2.Limit Order

python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.002 --price 65000

3.Stop Order

python cli.py --symbol BTCUSDT --side SELL --order_type STOP --quantity 0.002 --price 60000

## Sample Output
Order Request
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.002

Order Placed Successfully!
Order ID: 12237326802
Status: NEW
Executed Qty: 0.000
Avg Price: 0.00

Updated Order Status:
Status: NEW
Executed Qty: 0.000
Avg Price: 0.00

## Example log entry:
2026-02-13 12:30:10 - INFO - Request: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.002}

2026-02-13 12:30:11 - INFO - Response: {'orderId': 123456789, 'status': 'NEW'}

## Author
Param Shinde
