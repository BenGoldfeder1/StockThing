import pandas as pd
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Step 1: Get stock price data
def get_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={"APPL"}&apikey={"K34RPEJZOW4GWF8N"}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame.from_dict(data['TIME_SERIES_DAILY_ADJUSTED'], orient='index')
    df = df.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. volume': 'Volume'
    }).astype(float)
    df.index = pd.to_datetime(df.index)
    return df

# Step 2: Get sentiment data
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)['compound']

def get_sentiment_data(posts):
    sentiment_scores = []
    for post in posts:
        score = analyze_sentiment(post['text'])
        sentiment_scores.append({'date': post['date'], 'sentiment': score})
    df = pd.DataFrame(sentiment_scores)
    df['date'] = pd.to_datetime(df['date'])
    df = df.groupby(df['date'].dt.date).mean()
    return df

# Example posts data (replace with actual data scraping)
posts = [
    {'date': '2023-06-01', 'text': 'Great news about this stock!'},
    {'date': '2023-06-02', 'text': 'Not sure about the future of this stock.'},
    # More posts...
]

# Get data
stock_data = get_stock_data('AAPL', 'your_api_key')
sentiment_data = get_sentiment_data(posts)

# Merge data
merged_data = pd.merge(stock_data, sentiment_data, left_index=True, right_index=True, how='inner')

# Plot data
plt.figure(figsize=(10,5))
plt.plot(merged_data.index, merged_data['Close'], label='Stock Price')
plt.plot(merged_data.index, merged_data['sentiment'], label='Sentiment Score')
plt.legend()
plt.show()
