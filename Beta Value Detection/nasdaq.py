import yfinance as yf
from yahoo_fin import stock_info as si
import pandas as pd

# Get all stocks on NASDAQ
stonks = pd.DataFrame(si.tickers_nasdaq())
nasdaq_stocks = stonks[0].tolist()

# Loop through the entire list and update each object
for i in range(len(nasdaq_stocks)):
    nasdaq_stocks[i] = yf.Ticker(nasdaq_stocks[i])

# Create a list to store stock attributes
stock_attributes = []

# Iterate through each stock
for stock in nasdaq_stocks:
    # Get the stock attributes
    attributes = [
                  stock.info.get('symbol'),
                  stock.info.get('previousClose'),
                  stock.info.get('regularMarketOpen'),
                  stock.info.get('bid'),
                  stock.info.get('ask'),
                  stock.info.get('dayLow'),
                  stock.info.get('dayHigh'),
                  stock.info.get('52WeekLow'),
                  stock.info.get('52WeekHigh'),
                  stock.info.get('volume'),
                  stock.info.get('averageVolume'),
                  stock.info.get('marketCap'),
                  stock.info.get('beta'),
                  stock.info.get('trailingPE'),
                  stock.info.get('forwardPE'),
                  stock.info.get('dividendYield'),
                  stock.info.get('exDividendDate'),
                  stock.info.get('payoutRatio'),
                  stock.info.get('trailingAnnualDividendRate'),
                  stock.info.get('trailingAnnualDividendYield'),
                  stock.info.get('fiveYearAvgDividendYield'),
                  stock.info.get('dividendRate'),
                  stock.info.get('annualDividendRate'),
                  stock.info.get('dividendYield'),
                  stock.info.get('fiftyDayAverage'),
                  stock.info.get('twoHundredDayAverage'),
                  stock.info.get('trailingAnnualDividendRate'),
                  stock.info.get('trailingAnnualDividendYield'),
                  stock.info.get('averageDailyVolume10Day'),
                  stock.info.get('averageDailyVolume3Month'),
                  stock.info.get('fiftyTwoWeekLowChange'),
                  stock.info.get('fiftyTwoWeekLowChangePercent'),
                  stock.info.get('fiftyTwoWeekRange'),
                  stock.info.get('fiftyTwoWeekHighChange'),
                  stock.info.get('fiftyTwoWeekHighChangePercent'),
                  stock.info.get('fiftyTwoWeekLow'),
                  stock.info.get('fiftyTwoWeekHigh'),
                  stock.info.get('earningsTimestamp'),
                  stock.info.get('earningsTimestampStart'),
                  stock.info.get('earningsTimestampEnd'),
                  stock.info.get('trailingAnnualEps'),
                  stock.info.get('epsTrailingTwelveMonths'),
                  stock.info.get('epsForward'),
                  stock.info.get('sharesOutstanding'),
                  stock.info.get('floatShares'),
                  stock.info.get('sharesShort'),
                  stock.info.get('sharesShortPriorMonth'),
                  stock.info.get('shortRatio'),
                  stock.info.get('shortPercentOutstanding'),
                  stock.info.get('shortPercentFloat'),
                  stock.info.get('percentInsiders'),
                  stock.info.get('percentInstitutions'),
                  stock.info.get('forwardEps'),
                  stock.info.get('pegRatio'),
                  stock.info.get('lastSplitFactor'),
                  stock.info.get('lastSplitDate'),
                  stock.info.get('enterpriseToRevenue'),
                  stock.info.get('enterpriseToEbitda'),
                  stock.info.get('52WeekChange'),
                  stock.info.get('SandP52WeekChange'),
                  stock.info.get('lastDividendValue'),
                  stock.info.get('lastCapGain'),
                  stock.info.get('annualHoldingsTurnover'),
                  stock.info.get('enterpriseValue'),
                  stock.info.get('priceToSalesTrailing12Months'),
                  stock.info.get('priceToBook'),
                  stock.info.get('mostRecentQuarter'),
                  stock.info.get('netIncomeToCommon'),
                  stock.info.get('trailingEps'),
                  stock.info.get('forwardEps'),
                  stock.info.get('beta'),
                  stock.info.get('enterpriseValue'),
                  stock.info.get('priceHint'),
                  stock.info.get('trailingAnnualDividendRate'),
                  stock.info.get('trailingAnnualDividendYield'),
                  stock.info.get('fiveYearAvgDividendYield'),
                  stock.info.get('dividendRate'),
                  stock.info.get('annualDividendRate'),
                  stock.info.get('dividendYield'),
                  stock.info.get('financialCurrency')]
    
    # Add the stock attributes to the list
    stock_attributes.append(attributes)

# Create a DataFrame from the stock attributes list
df = pd.DataFrame(stock_attributes, columns=['ticker', 'previousClose', 'regularMarketOpen', 'bid', 'ask', 'dayLow', 'dayHigh', '52WeekLow', '52WeekHigh', 'volume', 'averageVolume', 'marketCap', 'beta', 'trailingPE', 'forwardPE', 'dividendYield', 'exDividendDate', 'payoutRatio', 'trailingAnnualDividendRate', 'trailingAnnualDividendYield', 'fiveYearAvgDividendYield', 'dividendRate', 'annualDividendRate', 'dividendYield', 'fiftyDayAverage', 'twoHundredDayAverage', 'trailingAnnualDividendRate', 'trailingAnnualDividendYield', 'averageDailyVolume10Day', 'averageDailyVolume3Month', 'fiftyTwoWeekLowChange', 'fiftyTwoWeekLowChangePercent', 'fiftyTwoWeekRange', 'fiftyTwoWeekHighChange', 'fiftyTwoWeekHighChangePercent', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'earningsTimestamp', 'earningsTimestampStart', 'earningsTimestampEnd', 'trailingAnnualEps', 'epsTrailingTwelveMonths', 'epsForward', 'sharesOutstanding', 'floatShares', 'sharesShort', 'sharesShortPriorMonth', 'shortRatio', 'shortPercentOutstanding', 'shortPercentFloat', 'percentInsiders', 'percentInstitutions', 'forwardEps', 'pegRatio', 'lastSplitFactor', 'lastSplitDate', 'enterpriseToRevenue', 'enterpriseToEbitda', '52WeekChange', 'SandP52WeekChange', 'lastDividendValue', 'lastCapGain', 'annualHoldingsTurnover', 'enterpriseValue', 'priceToSalesTrailing12Months', 'priceToBook', 'mostRecentQuarter', 'netIncomeToCommon', 'trailingEps', 'forwardEps', 'beta', 'enterpriseValue', 'priceHint', 'trailingAnnualDividendRate', 'trailingAnnualDividendYield', 'fiveYearAvgDividendYield', 'dividendRate', 'annualDividendRate', 'dividendYield', 'financialCurrency'])

# Save the DataFrame to a CSV file
df.to_csv('stock_attributes.csv', index=False)
with open('high_beta_stocks.txt', 'w') as file:
    for stock in high_beta_stocks:
        file.write(stock + '\n')