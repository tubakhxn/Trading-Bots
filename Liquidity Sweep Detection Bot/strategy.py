import numpy as np
import pandas as pd

def detect_liquidity_sweeps(df, window=10):
    swings = pd.DataFrame(index=df.index)
    swings['high'] = df['High'] if 'High' in df.columns else df['high']
    swings['low'] = df['Low'] if 'Low' in df.columns else df['low']
    swings['close'] = df['Close'] if 'Close' in df.columns else df['close']

    swings['swing_high'] = swings['high'][(swings['high'] == swings['high'].rolling(window, center=True).max())]
    swings['swing_low'] = swings['low'][(swings['low'] == swings['low'].rolling(window, center=True).min())]

    swings['bearish_sweep'] = False
    swings['bullish_sweep'] = False
    swings['bearish_sweep_zone'] = np.nan
    swings['bullish_sweep_zone'] = np.nan

    last_high_idx = None
    last_low_idx = None

    for i in range(window, len(swings)):
        # Bearish sweep: price breaks previous swing high, closes below it
        prev_highs = swings['swing_high'].iloc[:i].dropna()
        if len(prev_highs) > 0:
            last_high_idx = prev_highs.index[-1]
            last_high = prev_highs.iloc[-1]
            if swings['high'].iloc[i] > last_high and swings['close'].iloc[i] < last_high:
                swings.at[swings.index[i], 'bearish_sweep'] = True
                swings.at[swings.index[i], 'bearish_sweep_zone'] = last_high
        # Bullish sweep: price breaks previous swing low, closes above it
        prev_lows = swings['swing_low'].iloc[:i].dropna()
        if len(prev_lows) > 0:
            last_low_idx = prev_lows.index[-1]
            last_low = prev_lows.iloc[-1]
            if swings['low'].iloc[i] < last_low and swings['close'].iloc[i] > last_low:
                swings.at[swings.index[i], 'bullish_sweep'] = True
                swings.at[swings.index[i], 'bullish_sweep_zone'] = last_low
    return swings
