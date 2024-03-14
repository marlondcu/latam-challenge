import json
from datetime import datetime
from collections import defaultdict
from typing import List, Tuple
import time

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    start_time = time.time()  # Record the start time
    
    date_tweet_count = defaultdict(int)
    date_user_tweets = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r', encoding='utf-8') as json_file:
        for line in json_file:
            tweet = json.loads(line)
            date_str = tweet["date"][:10]  # Extract date part from the datetime string
            date_tweet_count[date_str] += 1
            date_user_tweets[date_str][tweet["user"]["username"]] += 1

    top_dates_users = []
    for date, user_tweets in date_user_tweets.items():
        top_user = max(user_tweets, key=user_tweets.get)
        top_dates_users.append((datetime.strptime(date, '%Y-%m-%d').date(), top_user))

    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time} seconds")

    return sorted(top_dates_users, key=lambda x: date_tweet_count[x[0]], reverse=True)[:10]

# Example usage:
file_path = "/Users/marlonoliveira/Downloads/farmers-protest-tweets-2021-2-4.json"
result = q1_time(file_path)
print(result)

# Optimizations made:

# Instead of using sorted twice, use a single sorted call on top_dates_users with a custom key function to prioritize dates by tweet count.
# Use max directly on user_tweets to find the top user, avoiding unnecessary conversion to items.
# These optimizations should result in a slightly faster execution time. Keep in mind that the performance gain might vary depending on the size of your dataset and specific conditions.