# StockThing

# We are using yfinance API. The general format is as follows:

import yfinance as yf

msft = yf.Ticker("MSFT")

print(msft.info)

# All data can be accessed via the .info dictionary and may be called as such, for example, EBITDA margins

print(msft.info['ebitdaMargins'])

# The programs connect as such:
# Beta Value detection >1 -> Sentiment Analysis -> DCF Program -> Other Programs
