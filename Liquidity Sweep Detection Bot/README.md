# Liquidity Sweep Detection Bot

## dev/creator: tubakhxn

---

## What is this project about?

This project is a Python-based quant tool for detecting liquidity sweeps (also known as stop hunts) in financial markets. It identifies moments when the price breaks previous swing highs or lows and quickly reverses, which can signal the presence of large players triggering stop-losses before moving the market in the opposite direction.

**Features:**
- Load price data from CSV or Yahoo Finance (yfinance)
- Identify swing highs/lows using a rolling window
- Detect liquidity sweeps (bullish and bearish)
- Generate buy/sell signals
- Visualize results with a professional, dark-themed matplotlib chart

**Output:**
- Chart saved as `outputs/liquidity_sweeps.png`

---

## How to fork and run

1. **Fork the repository**
   - Click the "Fork" button on GitHub to create your own copy.
2. **Clone your fork**
   - `git clone https://github.com/YOUR_USERNAME/Liquidity-Sweep-Detection-Bot.git`
3. **Navigate to the project folder**
   - `cd Liquidity-Sweep-Detection-Bot`
4. **Run the bot**
   - `python main.py --symbol BTC-USD --window 10`
   - Or use your own CSV: `python main.py --csv path/to/your.csv --window 10`

All dependencies are auto-installed at runtime.

---

## Relevant Wikipedia Links
- [Stop hunting](https://en.wikipedia.org/wiki/Stop_hunting)
- [Swing trading](https://en.wikipedia.org/wiki/Swing_trading)
- [Liquidity](https://en.wikipedia.org/wiki/Liquidity)
- [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
- [Yahoo! Finance](https://en.wikipedia.org/wiki/Yahoo!_Finance)
