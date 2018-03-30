import pandas as pd

def load_data():
    if __name__ == "__main__":
        data = pd.read_csv("hn_stories.csv")
        data.columns = ["submission_time", "upvotes", "url", "headline"]
        return data
