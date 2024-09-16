import pandas as pd
import numpy as np

def mean_reversion_strategy(data: pd.DataFrame, window: int = 20):
    data['mean'] = data['Close'].rolling(window=window).mean()
    data['signal'] = 0
    data['signal'][window:] = np.where(data['Close'][window:] > data['mean'][window:], -1, 1)
    return data
