# src/get_data.py
import os
import praw
import json
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

def load_reddit_api():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD")
    )

def scrape_subreddit(reddit, subreddit_name, limit=100):
    posts = []
    subreddit = reddit.subreddit(subreddit_name)
    for post in subreddit.hot(limit=limit):
        posts.append({
            'title': post.title,
            'text': post.selftext,
            'score': post.score,
            'created_utc': post.created_utc,
            'subreddit': subreddit_name,
            'id': post.id
        })
    return posts

def save_to_json(data, filename):
    os.makedirs('data/raw', exist_ok=True)
    with open(f'data/raw/{filename}', 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == '__main__':
    reddit = load_reddit_api()

    # Example emotion-related subreddits
    subreddits = ['happy', 'depression', 'offmychest', 'confession']

    for sub in subreddits:
        print(f"Scraping r/{sub}...")
        posts = scrape_subreddit(reddit, sub, limit=100)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        save_to_json(posts, f'reddit_{sub}_{timestamp}.json')
        print(f"Saved {len(posts)} posts from r/{sub}.")
