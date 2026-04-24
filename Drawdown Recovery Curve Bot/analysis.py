import numpy as np
import pandas as pd

def compute_cumulative_returns(df):
    df = df.copy()
    df['Return'] = df['Close'].pct_change().fillna(0)
    df['Cumulative'] = (1 + df['Return']).cumprod()
    return df

def compute_drawdown(df):
    df = df.copy()
    df['Peak'] = df['Cumulative'].cummax()
    df['Drawdown'] = (df['Cumulative'] - df['Peak']) / df['Peak']
    return df

def extract_drawdown_events(df):
    """
    Returns a list of dicts: {start, bottom, end, depth, duration}
    """
    events = []
    in_drawdown = False
    start_idx = None
    bottom_idx = None
    min_drawdown = 0
    for i, (idx, row) in enumerate(df.iterrows()):
        dd_val = row['Drawdown']
        # Robustly convert to float regardless of type
        try:
            dd = float(np.asarray(dd_val).item())
        except Exception:
            dd = float(dd_val)
        if not in_drawdown:
            if dd < 0:
                in_drawdown = True
                start_idx = idx
                min_drawdown = dd
                bottom_idx = idx
            # else: still at peak
        else:
            if dd < min_drawdown:
                min_drawdown = dd
                bottom_idx = idx
            if dd == 0:
                # Recovery
                end_idx = idx
                duration = (end_idx - start_idx).days
                events.append({
                    'start': start_idx,
                    'bottom': bottom_idx,
                    'end': end_idx,
                    'depth': min_drawdown,
                    'duration': duration
                })
                in_drawdown = False
                start_idx = None
                bottom_idx = None
                min_drawdown = 0
    return events
