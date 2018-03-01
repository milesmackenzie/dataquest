import pandas as pd
import matplotlib.pyplot as plt
from numpy import arange

# Reading in data and setting norm_reviews to columns
# ['FILM', 'RT_user_norm', 'Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue','Fandango_Stars']
# in reviews

reviews = pd.read_csv('fandango_scores.csv')
norm_reviews = reviews[['FILM', 'RT_user_norm', 'Metacritic_user_nom','IMDB_norm','Fandango_Ratingvalue','Fandango_Stars']]

# Specifying the position, the width and the height of the bars.
# Creating a single subplot and assigning the returned Figure object to
# fig and the returned Axes object to ax.

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)
plt.show()

# Generating bar plot as above.
# Setting x axis tick positions and labels, x and y axis labels
# and title to bar plot.

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.bar(bar_positions, bar_heights, 0.5)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_xticks(tick_positions)
ax.set_xlabel('Rating Source')
ax.set_ylabel('Average Rating')
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")


# Generating another bar plot. Switched orientation to horizontal requiring
# setting y-axis tick labels and positions instead of x-axis ticks.

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

fig, ax = plt.subplots()
ax.barh(bar_positions, bar_widths, 0.5)
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)
ax.set_ylabel('Rating Source')
ax.set_xlabel('Average Rating')
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")


# Generating scatter plot using .scatter()
# plotting Fandango_Ratingvalue on x-axis and
# RT_user_norm on y-axis

fig, ax = plt.subplots()

x_axis = norm_reviews['Fandango_Ratingvalue']
y_axis = norm_reviews['RT_user_norm']
ax.scatter(x_axis, y_axis)
ax.set_xlabel('Fandango')
ax.set_ylabel('Rotten Tomatoes')


# Generating two subplots to show switching of axes.
# Using plt.figure to set figsize and fig.add_subplot()
# to add each subplot

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

x_axis = norm_reviews['Fandango_Ratingvalue']
y_axis = norm_reviews['RT_user_norm']
ax1.scatter(x_axis, y_axis)
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')

x_axis = norm_reviews['RT_user_norm']
y_axis = norm_reviews['Fandango_Ratingvalue']
ax2.scatter(x_axis, y_axis)
ax2.set_xlabel('Rotten Tomatoes')
ax2.set_ylabel('Fandango')


# Generating three subplots and setting y and x limits 0 and 5

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['RT_user_norm'])
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)

ax2.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['Metacritic_user_nom'])
ax2.set_xlabel('Fandango')
ax2.set_ylabel('Metacritic')
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)

ax3.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['IMDB_norm'])
ax3.set_xlabel('Fandango')
ax3.set_ylabel('IMDB')
ax3.set_xlim(0, 5)
ax3.set_ylim(0, 5)
