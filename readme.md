# 🚀 Binance Futures Testnet Trading Bot

A Python-based CLI trading bot that interacts with the Binance Futures Testnet (USDT-M) to place MARKET, LIMIT, and STOP orders.

This project demonstrates API integration, structured code design, input validation, logging, and error handling.

---

## 📌 Features

- Place **MARKET**, **LIMIT**, and **STOP** orders
- Supports both **BUY** and **SELL**
- CLI-based interface using Click
- Input validation for all parameters
- Logging of API requests, responses, and errors
- Structured and reusable codebase
- Error handling for API and network failures

---

## 🛠️ Tech Stack

- Python 3.x
- python-binance
- Click (CLI)
- python-dotenv
- Logging module

---

## 📁 Project Structure

trading_bot/
│
├── bot/
│ ├── init.py
│ ├── client.py # Binance client wrapper
│ ├── orders.py # Order placement logic
│ ├── validators.py # Input validation
│ └── logging_config.py
│
├── cli.py # CLI entry point
├── config.py # Configuration (API keys, URLs)
├── requirements.txt
├── README.md
└── logs/
└── bot.log


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

bash
git clone https://github.com/your-username/binance-futures-trading-bot.git
cd binance-futures-trading-bot
## Install Dependencies
pip install -r requirements.txt
## Create .env File
Create a .env file in the root directory:

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
 Use Binance Futures Testnet API keys

##Testnet URL:
https://testnet.binancefuture.com

## Run the Application
Use the CLI commands below.

## Usage Examples
 Market Order
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.002
 Limit Order
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.002 --price 65000
 Stop Order (Bonus Feature)
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
## Logging
All API requests, responses, and errors are logged in:

logs/bot.log
##Example log entry:

2026-02-13 12:30:10 - INFO - Request: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.002}
2026-02-13 12:30:11 - INFO - Response: {'orderId': 123456789, 'status': 'NEW'}
## Validation & Error Handling
The application validates:

Side must be BUY or SELL

Order type must be MARKET, LIMIT, or STOP

Quantity must be greater than 0

Price is required for LIMIT and STOP orders

Minimum notional value (≥ 100 USDT)

Handles errors such as:

Invalid inputs

Binance API errors

Network failures

## Exchange Constraints
Minimum notional value: ~100 USDT

Limit price must follow Binance filters

Testnet orders may remain NEW if conditions are not met

## Assumptions
Binance Futures Testnet is used

Market prices are dynamic

Orders may not execute immediately on testnet

## Future Improvements
WebSocket integration for live price tracking

Automated trading strategies (Grid, DCA, Scalping)

UI dashboard (React / FastAPI)

Portfolio tracking

## Security
API keys are stored using environment variables

.env file is excluded from version control

## Requirements
python-binance==1.0.19
python-dotenv
click

## Submission Details
This project fulfills the following requirements:

✔ Place MARKET and LIMIT orders
✔ Support BUY and SELL
✔ CLI input handling
✔ Logging of requests and responses
✔ Error handling
✔ Modular code structure


## Author
Param Shinde

GitHub: https://github.com/paramshinde

LinkedIn: www.linkedin.com/in/param-shinde-data
