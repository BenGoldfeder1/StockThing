import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime

def get_reddit_posts(company_name, date, reddit):
    # Define the date range
    start_date = int(datetime.datetime.strptime(date, "%Y-%m-%d").timestamp())
    end_date = start_date + 86400  # Add one day (86400 seconds)
    
    # Fetch posts using the Reddit API
    posts = []
    for submission in reddit.subreddit("all").search(company_name, sort='new', time_filter='day'):
        if start_date <= submission.created_utc <= end_date:
            posts.append(submission.title + ' ' + submission.selftext)
    
    return posts

def analyze_sentiments(posts):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_results = {'positive': 0, 'negative': 0, 'neutral': 0}
    
    for post in posts:
        score = analyzer.polarity_scores(post)
        if score['compound'] > 0.05:
            sentiment_results['positive'] += 1
        elif score['compound'] < -0.05:
            sentiment_results['negative'] += 1
        else:
            sentiment_results['neutral'] += 1
            
    return sentiment_results

def main():
    company_name = input("Enter the company or stock name: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    
    # Reddit API credentials
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='YOUR_USER_AGENT'
    )
    
    posts = get_reddit_posts(company_name, date, reddit)
    
    if not posts:
        print("No posts found.")
        return
    
    sentiment_results = analyze_sentiments(posts)
    
    print(f"Number of posts: {len(posts)}")
    print("Sentiment Analysis Results:")
    print(f"Positive: {sentiment_results['positive']}")
    print(f"Negative: {sentiment_results['negative']}")
    print(f"Neutral: {sentiment_results['neutral']}")

if __name__ == "__main__":
    main()
