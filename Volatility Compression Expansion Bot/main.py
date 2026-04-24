import os
import sys
import importlib.util

# Auto-install required packages
REQUIRED = ['pandas', 'numpy', 'matplotlib', 'yfinance']
import subprocess
for pkg in REQUIRED:
    if importlib.util.find_spec(pkg) is None:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])

import pandas as pd
import numpy as np
import yfinance as yf
from indicators import bollinger_bands, detect_compression, detect_expansion_breakout
from visualize import plot_volatility_squeeze

def load_data(source, symbol=None, csv_path=None, period='1y'):
    if source == 'yfinance' and symbol:
        df = yf.download(symbol, period=period)
        df = df[['Close']].dropna()
    elif source == 'csv' and csv_path:
        df = pd.read_csv(csv_path, index_col=0, parse_dates=True)
        if 'Close' not in df.columns:
            raise ValueError('CSV must have a Close column')
        df = df[['Close']].dropna()
    else:
        raise ValueError('Invalid data source')
    return df

def main():
    # --- USER CONFIG ---
    DATA_SOURCE = 'yfinance'  # 'yfinance' or 'csv'
    SYMBOL = 'AAPL'           # Used if yfinance
    CSV_PATH = None           # Used if csv
    PERIOD = '1y'             # yfinance period
    WINDOW = 20
    NUM_STD = 2
    BANDWIDTH_PERCENTILE = 20
    MIN_COMPRESSION_LEN = 5
    MIN_EXPANSION = 1.2
    OUTPUT_PATH = os.path.join('outputs', 'volatility_squeeze.png')

    # --- LOAD DATA ---
    df = load_data(DATA_SOURCE, symbol=SYMBOL, csv_path=CSV_PATH, period=PERIOD)

    # --- INDICATORS ---
    bands = bollinger_bands(df, window=WINDOW, num_std=NUM_STD)
    compression = detect_compression(bands['bandwidth'], percentile=BANDWIDTH_PERCENTILE)
    breakout = detect_expansion_breakout(df, compression, bands['bandwidth'], min_inactive=MIN_COMPRESSION_LEN, min_expansion=MIN_EXPANSION)

    # --- VISUALIZE ---
    plot_volatility_squeeze(df, bands, compression, breakout, OUTPUT_PATH)
    print(f"Chart saved to {OUTPUT_PATH}")

if __name__ == '__main__':
    main()
