# Determining which words appear most often in the headlines.

import pandas as pd
from collections import Counter

def load_data():
    if __name__ == "__main__":
        data = pd.read_csv("hn_stories.csv")
        data.columns = ["submission_time", "upvotes", "url", "headline"]
        return data

strings = []
for item in load_data()['headline']:
    strings.append(item)

for item in strings:
    if str(item) == 'nan':
        strings.remove(item)

strings = " ".join(strings)
strings = strings.split()
strings = [x.lower() for x in strings]

counts = {}

for item in strings:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] =  1

top_100 = dict(Counter(counts).most_common(100))
print (top_100)
