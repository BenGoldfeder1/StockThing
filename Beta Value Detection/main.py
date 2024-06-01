import yfinance as yf
from yahoo_fin import stock_info as si
import pandas as pd

# Get all stocks on NASDAQ
stonks = pd.DataFrame( si.tickers_nasdaq() )
nasdaq_stocks = stonks[0].tolist()

# Loop through the entire list and update each object
for i in range(len(nasdaq_stocks)):
    nasdaq_stocks[i] = yf.Ticker(nasdaq_stocks[i])

# Create a list to store high beta stocks
high_beta_stocks = []

# Iterate through each stock
for stock in nasdaq_stocks:
    # Get the beta value
    beta = stock.info['beta']
    
    # Check if the beta value is greater than 1
    if beta > 1:
        # Add the stock symbol to the high beta stocks list
        high_beta_stocks.append(stock.ticker)
        
# Write the high beta stocks to a text file
with open('high_beta_stocks.txt', 'w') as file:
    for stock in high_beta_stocks:
        file.write(stock + '\n')