import pandas as pd
import matplotlib.pyplot as plt

# Reading in data and eliminating rows where the 'Year'
# is less than 1960.
# Generating histogram of results.
avengers = pd.read_csv("avengers.csv")

avengers['Year'].hist()
true_avengers = avengers[avengers['Year'] >= 1960]
true_avengers['Year'].hist()

# Writing function to count the number of deaths each superhero
# had and assinging a new column in true_avengers.

def clean_deaths(avengers):
    num_deaths = 0
    deaths = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']

    for item in deaths:
        itm = avengers[item]
        if pd.isnull(itm) or itm == 'NO':
            continue
        elif itm == 'YES':
            num_deaths += 1
    return num_deaths

true_avengers['Deaths'] = true_avengers.apply(clean_deaths, axis=1)

# Counting how many occurances where 'Years since joining' + 'Year' is equal to 2015.

joined_accuracy  = true_avengers[true_avengers['Year'] + true_avengers['Years since joining'] == 2015]
joined_accuracy_count = len(joined_accuracy)
print (joined_accuracy_count)
