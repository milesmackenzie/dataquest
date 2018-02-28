# reading in file

import pandas as pd
import numpy as np

fandango = pd.read_csv('fandango_score_comparison.csv')

# using .iloc[] to get first and last items

first_last = fandango.iloc[[0,145]]

# using "FILM" as the DataFrame index with .set_index

fandango_films = fandango.set_index("FILM",drop=False)


# selecting specific movies using list of movies

best_movies_ever = fandango_films.loc[["The Lazarus Effect (2015)", "Gett: The Trial of Viviane Amsalem (2015)", "Mr. Holmes (2015)"]]

# passing the lambda function to the DataFrame.apply() method

types = fandango_films.dtypes
float_columns = types[types.values == 'float64'].index
float_df = fandango_films[float_columns]

deviations = float_df.apply(lambda x: np.std(x))
double_df = float_df.apply(lambda x: x*2)
halved_df = float_df.apply(lambda x: x/2)

# filtering DataFrame down to two columns and returning a Series object containing
# the SD and mean of each movie's rating from RT_user_norm and Metacritic_user_nom.

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
