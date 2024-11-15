import yfinance as yahooFinance


def getStockValue(symbol, qty):
    stock = yahooFinance.Ticker(symbol)
    current_price = stock.info['currentPrice']
    return current_price * qty


def getPortfolio_Value(stocks):
    total_value = sum(getStockValue(
        stock['symbol'], stock['quantity']) for stock in stocks)
    return total_value


shares = [
    {"symbol": "AAPL", "quantity": 10},
    {"symbol": "GOOG", "quantity": 15},
    {"symbol": "TSLA", "quantity": 20},
    {"symbol": "AMZN", "quantity": 30},
]

portfolio_value = getPortfolio_Value(shares)

print(" Status of stocks portfolio:")
for stock in shares:
    stock_value = getStockValue(stock['symbol'], stock['quantity'])
    print(
        f"Having {stock['quantity']} shares of {stock['symbol']}, Total value: {stock_value}")

print(f"Total portfolio value: {portfolio_value}")