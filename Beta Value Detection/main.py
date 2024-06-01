import yfinance as yf
from yahoo_fin import stock_info as si

# Get all stocks on NASDAQ
nasdaq_stocks = get_nasdaq_stocks()

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