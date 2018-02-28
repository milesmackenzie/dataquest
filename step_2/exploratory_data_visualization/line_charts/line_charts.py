# reading in DataFrame and converting "DATE" column into series of datetime values

import pandas as pd

unrate = pd.read_csv("unrate.csv")
unrate["DATE"] = pd.to_datetime(unrate["DATE"])
print (unrate[0:12])

# importing matplotlib library as plt and dislpaying empty plot

import matplotlib.pyplot as plt
plt.plot()
print (plt.show())

# creating a plot with first 12 lines of "DATE" and "VALUE" colums
# visualizing unemployment rate from the year 1948

plt.plot(unrate["DATE"][0:12], unrate["VALUE"][0:12])

# rotating x axis with xticks()

plt.plot(unrate["DATE"][0:12], unrate["VALUE"][0:12])
plt.xticks(rotation=90)

# assigning axis labels and title using xlabel(), ylabel() and title()

plt.plot(unrate["DATE"][0:12], unrate["VALUE"][0:12])
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()
