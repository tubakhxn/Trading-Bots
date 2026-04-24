import os
import sys
import argparse
from data import load_price_data, ensure_packages
from analysis import compute_cumulative_returns, compute_drawdown, extract_drawdown_events
from visualize import plot_drawdown_recovery

def main():
    ensure_packages()
    parser = argparse.ArgumentParser(description='Drawdown Recovery Curve Bot')
    parser.add_argument('--source', choices=['csv', 'yfinance'], default='yfinance', help='Data source')
    parser.add_argument('--symbol', type=str, help='Ticker symbol for yfinance')
    parser.add_argument('--csv', type=str, help='Path to CSV file')
    parser.add_argument('--start', type=str, help='Start date (YYYY-MM-DD)')
    parser.add_argument('--end', type=str, help='End date (YYYY-MM-DD)')
    args = parser.parse_args()

    if args.source == 'csv':
        if not args.csv:
            print('CSV path required for csv source.')
            sys.exit(1)
        df = load_price_data('csv', csv_path=args.csv)
    else:
        if not args.symbol:
            print('Symbol required for yfinance source.')
            sys.exit(1)
        df = load_price_data('yfinance', symbol=args.symbol, start=args.start, end=args.end)

    df = compute_cumulative_returns(df)
    df = compute_drawdown(df)
    events = extract_drawdown_events(df)

    if not events:
        print('No drawdown events detected.')
        sys.exit(1)

    output_path = os.path.join('outputs', 'drawdown_recovery.png')
    plot_drawdown_recovery(events, df, output_path)
    print(f'Chart saved to {output_path}')

if __name__ == '__main__':
    main()
