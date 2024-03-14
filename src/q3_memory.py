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

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as json_file:
        with ThreadPoolExecutor() as executor:
            executor.map(lambda line: process_tweet(line, mention_counter), json_file)

    # Get the top 10 most mentioned users
    top_mentions = mention_counter.most_common(10)

    return top_mentions


# Example usage:
file_path = "/Users/marlonoliveira/Downloads/farmers-protest-tweets-2021-2-4.json"
result = q3_memory(file_path)
print(result)

# To optimize the code for memory usage, we can make some modifications to reduce the memory footprint. Specifically, we can avoid storing the entire list of mentions in memory and update the counter directly as we process each line

# In this version, the mention_counter is updated directly without storing the entire list of mentions in memory. This optimization helps reduce the memory footprint, especially when dealing with a large number of tweets in the JSON file.