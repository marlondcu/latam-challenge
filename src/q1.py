import json
from datetime import datetime
from collections import defaultdict
from typing import List, Tuple



def q1(file_path: str) -> List[Tuple[datetime.date, str]]:
    
    tweet_count_by_date = defaultdict(int) # dictionary to store tweet counts for each date
    top_user_by_date = defaultdict(str) # dictionary to store the user with the most posts for each date

    with open(file_path, 'r', encoding='utf-8') as file: # read JSON file line by line
        for line in file:
            tweet = json.loads(line) # parse each line as JSON
            tweet_date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S+00:00').date() # extract date and username
            username = tweet['user']['username']
            
            tweet_count_by_date[tweet_date] += 1 # update tweet count for this date
            
            # update top user for this date if necessary
            if tweet_count_by_date[tweet_date] == 1 or tweet_count_by_date[tweet_date] > tweet_count_by_date[max(tweet_count_by_date.keys())]:
                top_user_by_date[tweet_date] = username

    # sort dates by tweet count in descending order
    sorted_dates = sorted(tweet_count_by_date.items(), key=lambda x: x[1], reverse=True)[:10]

    # return top 10 dates with the most tweets and the user with the most posts for each date
    result = [(date, top_user_by_date[date]) for date, _ in sorted_dates]
    return result


# Result:
file_path = "farmers-protest-tweets-2021-2-4.json"
result = q1(file_path)
print(result)