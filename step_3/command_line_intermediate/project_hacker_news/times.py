import pandas as pd
from collections import Counter
from dateutil.parser import parse
import dateutil
import datetime

def load_data():
    if __name__ == "__main__":
        data = pd.read_csv("hn_stories.csv")
        data.columns = ["submission_time", "upvotes", "url", "headline"]
        return data

def get_time(x):
    i = dateutil.parser.parse(x)
    return i.hour

u = load_data()['submission_time'].apply(get_time)
print(u.value_counts())
