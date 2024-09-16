class Config:
    def __init__(self):
        self.api_key = "your_api_key"
        self.api_secret = "your_api_secret"
        self.base_currency = "USD"
        self.trading_pair = "BTC-USD"
        self.data_source = "yahoo"  # or "ccxt" for live trading

config = Config()
