import os
import pandas as pd
import yfinance as yf

def ensure_packages():
    import importlib
    import subprocess
    import sys
    pkgs = ['pandas', 'numpy', 'matplotlib', 'yfinance']
    for pkg in pkgs:
        try:
            importlib.import_module(pkg)
        except ImportError:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])


def load_price_data(source, symbol=None, csv_path=None, start=None, end=None):
    """
    Load price data from CSV or yfinance.
    Returns a DataFrame with a DatetimeIndex and a 'Close' column.
    """
    ensure_packages()
    if source == 'csv':
        if not csv_path or not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
        df = pd.read_csv(csv_path, parse_dates=True, index_col=0)
        if 'Close' not in df.columns:
            raise ValueError("CSV must have a 'Close' column.")
        df = df[['Close']]
    elif source == 'yfinance':
        if not symbol:
            raise ValueError("Symbol must be provided for yfinance.")
        df = yf.download(symbol, start=start, end=end, progress=False)
        if 'Close' not in df.columns:
            raise ValueError("Downloaded data must have a 'Close' column.")
        df = df[['Close']]
    else:
        raise ValueError("source must be 'csv' or 'yfinance'")
    df = df.dropna()
    df.index = pd.to_datetime(df.index)
    return df
