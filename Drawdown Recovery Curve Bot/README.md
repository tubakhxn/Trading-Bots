# Drawdown Recovery Curve Bot

## Dev/Creator = tubakhxn

## What is this project?

This project is a Python-based quant tool that analyzes how markets or strategies behave during drawdowns and how long they take to recover. It detects drawdown events, measures their depth and duration, and visualizes the relationship between drawdown severity and recovery time using clean, research-style charts.

**Features:**

* Load price data from CSV or Yahoo Finance (yfinance)
* Compute cumulative returns and rolling peak
* Calculate drawdown series
* Detect drawdown and recovery cycles
* Measure drawdown depth and recovery duration
* Visualize drawdown vs recovery using scatter + regression
* Save and display a quant-style dark-themed chart

## How to fork and run

1. **Fork this repository** using the GitHub interface ([How to fork a repo](https://en.wikipedia.org/wiki/Fork_%28software_development%29)).
2. **Clone your fork** to your local machine:

   ```sh
   git clone https://github.com/your-username/Drawdown-Recovery-Curve-Bot.git
   ```
3. **Navigate to the project folder** and run the bot:

   ```sh
   cd Drawdown-Recovery-Curve-Bot
   python main.py
   ```

   The bot will auto-install required dependencies (pandas, numpy, matplotlib, yfinance) if missing.
4. **View the output chart** in the `outputs/drawdown_recovery.png` file.

## Relevant Wikipedia Links

* [Drawdown (economics)](https://en.wikipedia.org/wiki/Drawdown_%28economics%29)
* [Maximum drawdown](https://en.wikipedia.org/wiki/Maximum_drawdown)
* [Time series](https://en.wikipedia.org/wiki/Time_series)
* [Regression analysis](https://en.wikipedia.org/wiki/Regression_analysis)
* [Python (programming language)](https://en.wikipedia.org/wiki/Python_%28programming_language%29)
* [Matplotlib](https://en.wikipedia.org/wiki/Matplotlib)
* [Pandas (software)](https://en.wikipedia.org/wiki/Pandas_%28software%29)
