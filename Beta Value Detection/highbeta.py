import yfinance as yf
from yahoo_fin import stock_info as si
import pandas as pd

# Get all stocks on NASDAQ
stonks = pd.DataFrame(si.tickers_nasdaq())
nasdaq_stocks = stonks[0].tolist()

# Loop through the entire list and update each object
for i in range(len(nasdaq_stocks)):
    nasdaq_stocks[i] = yf.Ticker(nasdaq_stocks[i])

# Create a list to store high beta stocks
high_beta_stocks = []

# Iterate through each stock and check if their 'beta' attribute is > 1
for stock in nasdaq_stocks:
    if stock.info['beta'] > 1:
        high_beta_stocks.append(stock.ticker)

# Write the high beta stocks to a text file
with open('/workspaces/StockThing/Beta Value Detection/high_beta_stocks.txt', 'w') as file:
    for stock in high_beta_stocks:
        file.write(stock + '\n')