import os
import json
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

RAW_DIR = 'data/raw'
PROCESSED_DIR = 'data/processed'
OUTPUT_FILE = 'reddit_cleaned.csv'

SUBREDDIT_LABEL_MAP = {
    'happy': 'joy',
    'depression': 'sadness',
    'offmychest': 'mixed',
    'confession': 'neutral'
}

def load_json_files(raw_dir):
    posts = []
    for filename in os.listdir(raw_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(raw_dir, filename)
            with open(filepath, 'r') as f:
                try:
                    data = json.load(f)
                    posts.extend(data)
                except json.JSONDecodeError:
                    logging.warning(f"Skipping malformed JSON: {filename}")
    return posts

def clean_posts(raw_posts):
    cleaned = []
    for post in raw_posts:
        title = post.get('title', '').strip()
        body = post.get('text', '').strip()
        text = f"{title} {body}".strip()

        if not text or text in ['[deleted]', '[removed]']:
            continue

        subreddit = post.get('subreddit', '').lower()
        label = SUBREDDIT_LABEL_MAP.get(subreddit, 'unknown')

        cleaned.append({
            'text': text,
            'subreddit': subreddit,
            'emotion_label': label,
            'score': post.get('score', 0)
        })
    return cleaned

def save_cleaned_posts(cleaned_posts, output_path):
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    df = pd.DataFrame(cleaned_posts)
    df.to_csv(output_path, index=False)
    logging.info(f"Saved {len(df)} cleaned posts to {output_path}")

if __name__ == '__main__':
    logging.info("Loading raw Reddit data...")
    raw_posts = load_json_files(RAW_DIR)

    logging.info(f"Cleaning {len(raw_posts)} posts...")
    cleaned = clean_posts(raw_posts)

    logging.info("Saving processed dataset...")
    save_cleaned_posts(cleaned, os.path.join(PROCESSED_DIR, OUTPUT_FILE))
