import json
from datetime import datetime
from collections import defaultdict
from typing import List, Tuple


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    date_tweet_count = defaultdict(int)
    top_dates_users = []

    with open(file_path, 'r', encoding='utf-8') as json_file:
        for line in json_file:
            tweet = json.loads(line)
            date_str = tweet["date"][:10]  # extract date part from the datetime string
            date_tweet_count[date_str] += 1
            user_tweet_count = date_tweet_count[date_str]

            if len(top_dates_users) < 10 or user_tweet_count > top_dates_users[-1][0]:
                top_dates_users.append((user_tweet_count, datetime.strptime(date_str, '%Y-%m-%d').date(), tweet["user"]["username"]))
                top_dates_users.sort(reverse=True)
                if len(top_dates_users) > 10:
                    top_dates_users.pop()

    return [(date, username) for _, date, username in top_dates_users]

# Result:
file_path = "farmers-protest-tweets-2021-2-4.json"
result = q1_memory(file_path)
print(result)