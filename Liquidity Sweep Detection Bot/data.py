import pandas as pd
import yfinance as yf
import os

def load_price_data(symbol=None, csv_path=None, start=None, end=None):
    if csv_path and os.path.exists(csv_path):
        df = pd.read_csv(csv_path, parse_dates=[0])
        df.columns = [c.lower() for c in df.columns]
        if 'date' in df.columns:
            df = df.rename(columns={'date': 'datetime'})
        if 'datetime' not in df.columns:
            df['datetime'] = pd.to_datetime(df.iloc[:,0])
        df = df.set_index('datetime')
        return df
    elif symbol:
        df = yf.download(symbol, start=start, end=end, progress=False)
        if df.empty:
            return None
        df = df.rename_axis('datetime').reset_index().set_index('datetime')
        return df
    else:
        return None
