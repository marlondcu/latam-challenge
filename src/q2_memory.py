import json
import re
from collections import Counter
from typing import List, Tuple

# precompile the regex pattern for extracting emojis
emoji_pattern = re.compile(r'\uD83C[\uDF00-\uDFFF]|\uD83D[\uDC00-\uDDFF]|\uD83E[\uDD00-\uDDFF]|[\u2600-\u2B55]')

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as json_file:
        for line in json_file:
            tweet = json.loads(line)
            # iterate over the emojis in the tweet and update the counter
            for emoji in emoji_pattern.finditer(tweet["content"]):
                emoji_counter[emoji.group()] += 1

    top_emojis = emoji_counter.most_common(10) # get the top 10 most used emojis
    return top_emojis

# Example usage:
file_path = "farmers-protest-tweets-2021-2-4.json"
result = q2_memory(file_path)
print(result)