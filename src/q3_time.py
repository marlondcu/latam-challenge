import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

def extract_mentions(text: str) -> List[str]:
    mention_pattern = r'@(\w+)'  # Adjust the regex pattern as needed
    mentions = re.findall(mention_pattern, text)
    return mentions

def process_tweet(line, mention_counter):
    tweet = json.loads(line)
    mentions = extract_mentions(tweet["content"])
    mention_counter.update(mentions)

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as json_file:
        with ThreadPoolExecutor() as executor:
            executor.map(lambda line: process_tweet(line, mention_counter), json_file)

    # Get the top 10 most mentioned users
    top_mentions = mention_counter.most_common(10)

    return top_mentions

# Example usage:
file_path = "/Users/marlonoliveira/Downloads/farmers-protest-tweets-2021-2-4.json"
result = q3_time(file_path)
print(result)

# This version uses ThreadPoolExecutor to parallelize the processing of tweets. The process_tweet function extracts mentions from each tweet, and the ThreadPoolExecutor efficiently distributes the workload across multiple threads.

# Note: The effectiveness of parallelization depends on the number of available CPU cores and the nature of the processing tasks. Adjust the regex pattern (mention_pattern) based on your specific dataset.