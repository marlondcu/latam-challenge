#from typing import List, Tuple
#from datetime import datetime

import json
from datetime import datetime
from collections import defaultdict
from typing import List, Tuple

#def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

def q1(file_path: str) -> List[Tuple[datetime.date, str]]:
    date_tweet_count = defaultdict(int)
    date_user_tweets = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r', encoding='utf-8') as json_file:
        for line in json_file:
            tweet = json.loads(line)
            date_str = tweet["date"][:10]  # Extract date part from the datetime string
            date_tweet_count[date_str] += 1
            date_user_tweets[date_str][tweet["user"]["username"]] += 1


    top_dates_users = []
    for date, count in sorted(date_tweet_count.items(), key=lambda x: x[1], reverse=True)[:10]:
        top_user = max(date_user_tweets[date].items(), key=lambda x: x[1])[0]
        top_dates_users.append((datetime.strptime(date, '%Y-%m-%d').date(), top_user))

    return top_dates_users

# Example usage:
file_path = "/Users/marlonoliveira/Downloads/farmers-protest-tweets-2021-2-4.json"
result = q1(file_path)
print(result)