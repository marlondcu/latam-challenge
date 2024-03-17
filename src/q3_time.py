import json
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

def extract_mentions(text: str) -> List[str]:
    # extract mentions (@) using a simple regex pattern
    mention_pattern = r'@(\w+)'
    mentions = re.findall(mention_pattern, text)
    return mentions

def process_tweets(lines): # process the tweets
    mention_counter = Counter()
    for line in lines:
        tweet = json.loads(line)
        mentions = extract_mentions(tweet["content"]) # exctract mentions
        mention_counter.update(mentions)
    return mention_counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as json_file: # read lines from file
        lines = json_file.readlines()

    # determine the number of workers for ThreadPoolExecutor
    num_workers = min(32, len(lines))  # set a maximum number of workers to prevent excessive resource usage

    # Divide the lines into chunks for parallel processing
    chunk_size = len(lines) // num_workers
    chunks = [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]
   
    with ThreadPoolExecutor(max_workers=num_workers) as executor:  # process tweets using ThreadPoolExecutor
        results = executor.map(process_tweets, chunks)
    
    for result in results: # combine results
        mention_counter.update(result)

    top_mentions = mention_counter.most_common(10) # get the top 10 most mentioned users
    return top_mentions

# Example usage:
file_path = "farmers-protest-tweets-2021-2-4.json"
result = q3_time(file_path)
print(result)