# Determining which urls submit the most.

import pandas as pd
from collections import Counter

def load_data():
    if __name__ == "__main__":
        data = pd.read_csv("hn_stories.csv")
        data.columns = ["submission_time", "upvotes", "url", "headline"]
        return data

domains = {}

for item in load_data()['url']:
    if item in domains:
        domains[item] += 1
    else:
        domains[item] = 1

top_100 = dict(Counter(domains).most_common(100))

print (top_100)
