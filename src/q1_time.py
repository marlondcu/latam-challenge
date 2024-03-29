import json
from datetime import datetime
from collections import defaultdict
from typing import List, Tuple

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    tweets = []

    with open(file_path, 'r', encoding='utf-8') as json_file: # load all tweets into memory
        for line in json_file:
            tweet = json.loads(line)
            tweets.append(tweet)

    # process tweets
    date_tweet_count = defaultdict(int)
    date_user_tweets = defaultdict(lambda: defaultdict(int))

    for tweet in tweets:
        date_str = tweet["date"][:10]  # extract date part from the datetime string
        date_tweet_count[date_str] += 1
        date_user_tweets[date_str][tweet["user"]["username"]] += 1  # extract user part from the string

    top_dates_users = []
    for date, user_tweets in date_user_tweets.items():
        top_user = max(user_tweets, key=user_tweets.get)
        top_dates_users.append((datetime.strptime(date, '%Y-%m-%d').date(), top_user)) # put in the expected format 

    return sorted(top_dates_users, key=lambda x: date_tweet_count[x[0]], reverse=True)[:10]

# Result:
file_path = "farmers-protest-tweets-2021-2-4.json"
result = q1_time(file_path)
print(result)