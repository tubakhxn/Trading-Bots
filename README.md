# Trading Bots Collection

## Dev/Creator = tubakhxn

## What is this?

This repository contains a collection of Python-based quantitative trading bots designed to explore different market behaviors using data-driven approaches. Each bot focuses on a specific concept such as risk, volatility, or liquidity, and produces clean, research-style visualizations using matplotlib.

---

## 1. Drawdown Recovery Curve Bot

### What is this project?

This bot analyzes how deep market drawdowns go and how long they take to recover. It helps visualize the relationship between drawdown severity and recovery time.

**Features:**

* Computes cumulative returns and drawdowns
* Detects drawdown and recovery cycles
* Measures drawdown depth and recovery duration
* Visualizes drawdown vs recovery using scatter plots

---

## 2. Volatility Compression Expansion Bot

### What is this project?

This bot detects volatility squeeze phases and identifies breakout movements when the market transitions from low to high volatility.

**Features:**

* Computes Bollinger Bands and bandwidth
* Identifies low volatility compression zones
* Detects expansion breakouts
* Visualizes squeeze and breakout phases on price charts

---

## 3. Liquidity Sweep Detection Bot

### What is this project?

This bot detects liquidity sweeps (stop hunts), where price breaks key levels and quickly reverses, often signaling potential trading opportunities.

**Features:**

* Identifies swing highs and lows
* Detects bullish and bearish liquidity sweeps
* Generates buy/sell signals
* Visualizes sweeps on a dark-themed price chart

---

## How to fork and run

1. **Fork this repository** using the GitHub interface ([How to fork a repo](https://en.wikipedia.org/wiki/Fork_%28software_development%29)).

2. **Clone your fork** to your local machine:

   ```sh
   git clone https://github.com/your-username/trading-bots-collection.git
   ```

3. **Navigate to the project folder**:

   ```sh
   cd trading-bots-collection
   ```

4. **Run any bot**:

   ```sh
   python main.py
   ```

   Each bot will auto-install required dependencies (pandas, numpy, matplotlib, yfinance) if missing.

5. **View outputs** in the `outputs/` folder.

---

## Relevant Wikipedia Links

* [Drawdown (economics)](https://en.wikipedia.org/wiki/Drawdown_%28economics%29)
* [Volatility (finance)](https://en.wikipedia.org/wiki/Volatility_%28finance%29)
* [Bollinger Bands](https://en.wikipedia.org/wiki/Bollinger_Bands)
* [Liquidity](https://en.wikipedia.org/wiki/Liquidity)
* [Swing trading](https://en.wikipedia.org/wiki/Swing_trading)
* [Python (programming language)](https://en.wikipedia.org/wiki/Python_%28programming_language%29)
* [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
* [Pandas (software)](https://en.wikipedia.org/wiki/Pandas_%28software%29)
