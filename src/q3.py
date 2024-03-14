import json
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple
import re

def extract_mentions(text: str) -> List[str]:
    # Extract mentions (@) using a simple regex pattern
    mention_pattern = r'@(\w+)'
    mentions = re.findall(mention_pattern, text)
    return mentions

def process_tweet(line, mention_counter):
    tweet = json.loads(line)
    mentions = extract_mentions(tweet["content"])
    mention_counter.update(mentions)

def q3(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as json_file:
        with ThreadPoolExecutor() as executor:
            executor.map(lambda line: process_tweet(line, mention_counter), json_file)

    # Get the top 10 most mentioned users
    top_mentions = mention_counter.most_common(10)

    return top_mentions

# Example usage:
file_path = "/Users/marlonoliveira/Downloads/farmers-protest-tweets-2021-2-4.json"
result = q3(file_path)
print(result)

# In this code, we extract mentions (@) from each tweet and update the Counter for each user. The q3 function then returns the top 10 users based on the count of mentions.

# Please adjust the mention extraction pattern (mention_pattern) based on your specific dataset, as Twitter mentions can include alphanumeric characters and underscores. This pattern captures mentions without considering the full Twitter username constraints.