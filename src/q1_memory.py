import json
from datetime import datetime
from collections import defaultdict
from typing import List, Tuple

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
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

    return sorted(top_dates_users, key=lambda x: date_tweet_count[x[0]], reverse=True)[:10]
