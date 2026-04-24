import sys
import subprocess
import importlib

def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)

for pkg in ["pandas", "numpy", "matplotlib", "yfinance"]:
    install_and_import(pkg)

import argparse
from data import load_price_data
from strategy import detect_liquidity_sweeps
from visualize import plot_liquidity_sweeps
import os

def main():
    parser = argparse.ArgumentParser(description="Liquidity Sweep Detection Bot")
    parser.add_argument("--symbol", type=str, help="Ticker symbol (for yfinance)")
    parser.add_argument("--csv", type=str, help="Path to CSV file (optional)")
    parser.add_argument("--window", type=int, default=10, help="Swing high/low window size")
    parser.add_argument("--output", type=str, default="outputs/liquidity_sweeps.png", help="Output image path")
    parser.add_argument("--start", type=str, default=None, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, default=None, help="End date (YYYY-MM-DD)")
    args = parser.parse_args()

    os.makedirs("outputs", exist_ok=True)

    df = load_price_data(symbol=args.symbol, csv_path=args.csv, start=args.start, end=args.end)
    if df is None or len(df) == 0:
        print("No data loaded. Exiting.")
        return

    swings = detect_liquidity_sweeps(df, window=args.window)
    plot_liquidity_sweeps(df, swings, output_path=args.output)
    print(f"Chart saved to {args.output}")

if __name__ == "__main__":
    main()
