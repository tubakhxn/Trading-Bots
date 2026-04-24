# Volatility Compression Expansion Bot

## What is this project?
This project is a Python-based quant tool that detects volatility squeeze phases in financial time series before large price moves. It uses Bollinger Bands to identify periods of low volatility (compression) and marks breakout points when volatility expands. The bot visualizes these phases on a dark-themed chart, highlighting compression zones and breakout points for easy analysis.

**Features:**
- Load price data from CSV or Yahoo Finance (yfinance)
- Compute Bollinger Bands and Bandwidth
- Identify volatility compression (bottom 20% bandwidth)
- Detect and mark expansion breakouts
- Save and display a quant-style chart

## How to fork and run
1. **Fork this repository** using the GitHub interface ([How to fork a repo](https://en.wikipedia.org/wiki/Fork_(software_development))).
2. **Clone your fork** to your local machine:
   ```sh
   git clone https://github.com/your-username/Volatility-Compression-Expansion-Bot.git
   ```
3. **Navigate to the project folder** and run the bot:
   ```sh
   cd Volatility-Compression-Expansion-Bot
   python main.py
   ```
   The bot will auto-install required dependencies (pandas, numpy, matplotlib, yfinance) if missing.
4. **View the output chart** in the `outputs/volatility_squeeze.png` file.

## Dev/Creator
### tubakhxn

## Relevant Wikipedia Links
- [Bollinger Bands](https://en.wikipedia.org/wiki/Bollinger_Bands)
- [Volatility (finance)](https://en.wikipedia.org/wiki/Volatility_(finance))
- [Fork (software development)](https://en.wikipedia.org/wiki/Fork_(software_development))
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
- [Pandas (software)](https://en.wikipedia.org/wiki/Pandas_(software))
