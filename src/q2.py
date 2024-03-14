#from typing import List, Tuple
#from datetime import datetime


import json
from collections import Counter
from typing import List, Tuple
import re 

def extract_emojis(text: str) -> List[str]:
    emoji_pattern = r'\uD83C[\uDF00-\uDFFF]|\uD83D[\uDC00-\uDDFF]|\uD83E[\uDD00-\uDDFF]|[\u2600-\u2B55]'
    emojis = [match.group() for match in re.finditer(emoji_pattern, text)]
    return emojis

def q2(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as json_file:
        for line in json_file:
            tweet = json.loads(line)
            emojis = extract_emojis(tweet["content"])
            emoji_counter.update(emojis)

    # Get the top 10 most used emojis
    top_emojis = emoji_counter.most_common(10)

    return top_emojis


# Example usage:
file_path = "/Users/marlonoliveira/Downloads/farmers-protest-tweets-2021-2-4.json"
result = q2(file_path)
print(result)