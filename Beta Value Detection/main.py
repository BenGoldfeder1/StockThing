import yfinance as yf
import yfinance as yf
from yahoo_fin import stock_info as si

def get_beta_values(stocks):
    beta_values = {}
    for stock in stocks:
        try:
            data = yf.download(stock, start='2023-01-01', end='2023-12-31')
            beta = data['Close'].pct_change().cov(data['Close'].pct_change('SPY'))
            beta_values[stock] = beta
        except:
            print(f"Failed to get beta value for {stock}")
    
    return beta_values

def save_high_beta_stocks(beta_values, threshold, output_file):
    high_beta_stocks = [stock for stock, beta in beta_values.items() if beta > threshold]
    with open(output_file, 'w') as file:
        for stock in high_beta_stocks:
            file.write(stock + '\n')

# List of stocks to get beta values for
def get_nasdaq_stocks():
    nasdaq_stocks = si.tickers_nasdaq()
    return nasdaq_stocks

# List of stocks to get beta values for
stocks = get_nasdaq_stocks()

# Get beta values for the stocks
beta_values = get_beta_values(stocks)

# Save stocks with beta value over 1 to a text file
save_high_beta_stocks(beta_values, 1, 'beta>1stocks.txt')