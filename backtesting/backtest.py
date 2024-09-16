import pandas as pd

def backtest(strategy, data: pd.DataFrame, initial_capital: float = 10000):
    data = strategy(data)
    data['returns'] = data['Close'].pct_change()
    data['strategy_returns'] = data['signal'].shift(1) * data['returns']
    data['portfolio_value'] = (1 + data['strategy_returns']).cumprod() * initial_capital
    return data
