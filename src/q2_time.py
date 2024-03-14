import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

def extract_emojis(text: str) -> List[str]:
    emoji_pattern = r'\uD83C[\uDF00-\uDFFF]|\uD83D[\uDC00-\uDDFF]|\uD83E[\uDD00-\uDDFF]|[\u2600-\u2B55]'
    emojis = [match.group() for match in re.finditer(emoji_pattern, text)]
    return emojis

def process_tweet(line):
    tweet = json.loads(line)
    emojis = extract_emojis(tweet["content"])
    return emojis

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as json_file:
        with ThreadPoolExecutor() as executor:
            emojis_lists = list(executor.map(process_tweet, json_file))

    for emojis in emojis_lists:
        emoji_counter.update(emojis)

    # Get the top 10 most used emojis
    top_emojis = emoji_counter.most_common(10)

    return top_emojis

# Example usage:
file_path = "/Users/marlonoliveira/Downloads/farmers-protest-tweets-2021-2-4.json"
result = q2_time(file_path)
print(result)


#This modification uses the ThreadPoolExecutor to concurrently process tweets and extract emojis, which can improve the overall execution time, especially when dealing with a large number of tweets. Keep in mind that the effectiveness of parallelization depends on factors such as the number of available CPU cores and the nature of the processing tasks.
