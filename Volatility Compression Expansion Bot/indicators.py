import numpy as np
import pandas as pd

def bollinger_bands(df, window=20, num_std=2):
    """
    Calculate Bollinger Bands and Bandwidth.
    Returns DataFrame with columns: 'middle', 'upper', 'lower', 'bandwidth'
    """
    # Ensure all are 1D Series, not DataFrames
    close = df['Close'] if isinstance(df, pd.DataFrame) else df
    # Flatten to 1D if any are 2D
    def flatten(s):
        arr = np.asarray(s)
        if arr.ndim == 2 and arr.shape[1] == 1:
            return pd.Series(arr[:,0], index=s.index)
        return s
    middle = flatten(close.rolling(window).mean())
    std = flatten(close.rolling(window).std())
    upper = flatten(middle + num_std * std)
    lower = flatten(middle - num_std * std)
    bandwidth = flatten((upper - lower) / middle)
    return pd.DataFrame({
        'middle': middle,
        'upper': upper,
        'lower': lower,
        'bandwidth': bandwidth
    }, index=df.index)

def detect_compression(bandwidth, percentile=20):
    """
    Identify compression zones where bandwidth is in the bottom percentile.
    Returns a boolean Series.
    """
    threshold = np.nanpercentile(bandwidth, percentile)
    return bandwidth < threshold

def detect_expansion_breakout(df, compression, bandwidth, min_inactive=5, min_expansion=1.2):
    """
    Detect breakout points after compression zones.
    Returns a boolean Series for breakout points.
    """
    breakout = np.zeros(len(df), dtype=bool)
    in_compression = False
    comp_start = 0
    for i in range(1, len(df)):
        if compression.iloc[i] and not in_compression:
            in_compression = True
            comp_start = i
        elif not compression.iloc[i] and in_compression:
            # Expansion: bandwidth increases by min_expansion x from compression mean
            comp_bw = bandwidth.iloc[comp_start:i]
            if len(comp_bw) >= min_inactive:
                comp_mean = np.nanmean(comp_bw)
                if bandwidth.iloc[i] > comp_mean * min_expansion:
                    breakout[i] = True
            in_compression = False
    return pd.Series(breakout, index=df.index)
