import ccxt
from config.config import config

def execute_trade(signal: int):
    exchange = ccxt.binance({
        'apiKey': config.api_key,
        'secret': config.api_secret,
    })

    if signal == 1:
        order = exchange.create_market_buy_order(config.trading_pair, 1)
    elif signal == -1:
        order = exchange.create_market_sell_order(config.trading_pair, 1)

    return order
