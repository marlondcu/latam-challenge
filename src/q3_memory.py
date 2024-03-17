import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple


def extract_mentions(text: str, mention_counter: Counter) -> None:
    mention_pattern = r'@(\w+)'  # regex pattern
    mentions = re.findall(mention_pattern, text)
    mention_counter.update(mentions)

def process_tweet(line, mention_counter): # process the tweets
    tweet = json.loads(line)
    extract_mentions(tweet["content"], mention_counter) # extract the mention

def q3_memory(file_path: str) -> List[Tuple[str, int]]: 
    mention_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as json_file:
        with ThreadPoolExecutor() as executor: # using ThreadPoolExecutor to improve memory usage
            for line in json_file:
                executor.submit(process_tweet, line, mention_counter)

    top_mentions = mention_counter.most_common(10) # get the top 10 most mentioned users
    return top_mentions

# Example usage:
file_path = "farmers-protest-tweets-2021-2-4.json"
result = q3_memory(file_path)
print(result)