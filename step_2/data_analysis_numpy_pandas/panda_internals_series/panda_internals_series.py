

# slicing and printing firts five items in the FILM and RottenTomatoes column
import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')

series_film = fandango["FILM"]
print (series_film[0:5])
series_rt = fandango["RottenTomatoes"]
print (series_rt[0:5])

#indexing by string values using Series
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values

series_custom = pd.Series(rt_scores, index=film_names)
print(series_custom[['Minions (2015)', 'Leviathan (2014)']])

# using internal integer index to slice lines 5-10 in series_custom

fiveten = series_custom[5:11]

# sorted original index and passed reindex() to sort by index

original_index = series_custom.index
sorted_by_index = (sorted(original_index))
sorted_by_index = series_custom.reindex(sorted_by_index)

# sorted by index and values using sort_index() and sort_values()

sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()

# normalizing series_custom to  0-5 scale by dividing each score by 20

series_normalized = (series_custom/20)

# passing boolean series into original series object to get movie names
# of ratings between 50 and 75

both_criteria = series_custom[(series_custom > 50)&(series_custom < 75)]

# using two series objects to calculate mean of user and critic ratings
# for each film

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])
rt_mean = (rt_critics + rt_users) / 2

print (rt_mean)
