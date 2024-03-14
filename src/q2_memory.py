import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

def extract_emojis(text: str) -> List[str]:
    emoji_pattern = r'\uD83C[\uDF00-\uDFFF]|\uD83D[\uDC00-\uDDFF]|\uD83E[\uDD00-\uDDFF]|[\u2600-\u2B55]'
    emojis = [match.group() for match in re.finditer(emoji_pattern, text)]
    return emojis

def process_tweet(line, emoji_counter):
    tweet = json.loads(line)
    emojis = extract_emojis(tweet["content"])
    emoji_counter.update(emojis)

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as json_file:
        with ThreadPoolExecutor() as executor:
            executor.map(lambda line: process_tweet(line, emoji_counter), json_file)

    # Get the top 10 most used emojis
    top_emojis = emoji_counter.most_common(10)

    return top_emojis


# Example usage:
file_path = "/Users/marlonoliveira/Downloads/farmers-protest-tweets-2021-2-4.json"
result = q2_memory(file_path)
print(result)

# In this version, we process each line individually, and as soon as we extract the emojis from a tweet, we update the Counter. This way, we avoid keeping a large list of emojis in memory.

# This optimization should help reduce memory usage, especially when dealing with a large number of tweets in the JSON file.