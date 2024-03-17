import json
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple
import re

def extract_mentions(text: str) -> List[str]:
    # extract mentions (@) using a simple regex pattern
    mention_pattern = r'@(\w+)'
    mentions = re.findall(mention_pattern, text)
    return mentions

def process_tweet(line, mention_counter):  # process the tweets
    tweet = json.loads(line)
    mentions = extract_mentions(tweet["content"]) #extract the content
    mention_counter.update(mentions)

def q3(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as json_file:
        with ThreadPoolExecutor() as executor:
            executor.map(lambda line: process_tweet(line, mention_counter), json_file)

    top_mentions = mention_counter.most_common(10) # get the top 10 most mentioned users
    return top_mentions

# Example usage:
file_path = "farmers-protest-tweets-2021-2-4.json"
result = q3(file_path)
print(result)