import yfinance as yf
from strategies.mean_reversion import mean_reversion_strategy
from backtesting.backtest import backtest

if __name__ == "__main__":
    data = yf.download("AAPL", start="2023-01-01", end="2025-01-01")
    result = backtest(mean_reversion_strategy, data)
    print(result.tail(25))
