# Reading in data and using Series.value_counts() to count
# JJ (Juvenile justice facility) and SCH_STATUS_MAGNET (magnet school).
# Generating pivot tables for total enrollment by gender for a JJ facility and
# magnet school

import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")
    jj = data["JJ"].value_counts()
    magnet = data["SCH_STATUS_MAGNET"].value_counts()
    p1 = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
    p2 = pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="SCH_STATUS_MAGNET", aggfunc="sum")
