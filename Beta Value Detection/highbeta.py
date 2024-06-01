import yfinance as yf
from yahoo_fin import stock_info as si
import pandas as pd

# Get all stocks on NASDAQ
stonks = pd.DataFrame(si.tickers_nasdaq())
nasdaq_stocks = stonks[0].tolist()

# Loop through the entire list and update each object
for i in range(len(nasdaq_stocks)):
    nasdaq_stocks[i] = yf.Ticker(nasdaq_stocks[i])

# Loop through the entire list and get rid of the ones that don't have a ticker
for stock in nasdaq_stocks:
    if not hasattr(stock.info, 'symbol'):
        nasdaq_stocks.remove(stock)

# Create a list to store high beta stocks
high_beta_stocks = []

with open('/workspaces/StockThing/Beta Value Detection/high_beta_stocks.txt', 'w') as file:
    for stock in nasdaq_stocks:
        if ('beta' in stock.info) and ('marketCap' in stock.info):
            if (stock.info['beta'] > 1) and (stock.info['marketCap'] > 50000000):
                high_beta_stocks.append(stock.ticker)
                file.write(stock.info['symbol'] + '\n')

# Write the high beta stocks to a text file
# with open('/workspaces/StockThing/Beta Value Detection/high_beta_stocks.txt', 'w') as file:
#    for stock in high_beta_stocks:
#        file.write(stock + '\n')