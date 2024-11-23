import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

# Set up your Twitter API keys
bearer_token = os.getenv("twitter_bearer_token")

# Authenticate with Tweepy
twitter_client = tweepy.Client(bearer_token=bearer_token)

def fetch_recent_tweets(query, max_results=10):
    try:
        # Search recent tweets
        response = twitter_client.search_recent_tweets(
            query=query,
            max_results=max_results,  # Maximum is 100 per request
            tweet_fields=["created_at", "text", "author_id"]
        )
        # Collect tweet data
        tweets = response.data if response.data else []
        return tweets
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []

# Example usage
tweets = fetch_recent_tweets("#Modi")
for tweet in tweets:
    print(f"Tweet ID: {tweet.id}, Text: {tweet.text}")
