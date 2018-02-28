# importing matplotlib and reading in 'unrate.csv'
# converting unrate['DATE'] column to datetime

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])

# plotting unemployment data for 1948 with axis labels and title

plt.plot(unrate['DATE'][0:12],unrate['VALUE'][0:12])
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")

# adding a figure and empty subplots with nrows, ncolumns and plot number

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

# producing subplots from the years 1948 and 1949

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate['DATE'][0:12],unrate['VALUE'][0:12])
ax2.plot(unrate['DATE'][12:24],unrate['VALUE'][12:24])

# adding figsize of 12 by 5 to horizontally extend subplots
# so that the x-axis labels are more readable, instead of rotating

fig = plt.figure(figsize=(12,5))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])

# adding subplots for the first 5 years of the data


fig = plt.figure(figsize=(12,12))
ax1 = fig.add_subplot(5,1,1)
ax2 = fig.add_subplot(5,1,2)
ax3 = fig.add_subplot(5,1,3)
ax4 = fig.add_subplot(5,1,4)
ax5 = fig.add_subplot(5,1,5)
ax1.plot(unrate['DATE'][0:12],unrate['VALUE'][0:12])
ax2.plot(unrate['DATE'][12:24],unrate['VALUE'][12:24])
ax3.plot(unrate['DATE'][24:36],unrate['VALUE'][24:36])
ax4.plot(unrate['DATE'][36:48],unrate['VALUE'][36:48])
ax5.plot(unrate['DATE'][48:60],unrate['VALUE'][48:60])


# answer from dataquest for more efficient code:

fig = plt.figure(figsize=(12,12))

for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['VALUE'])

# removing the year from the x axis to plot multiple years on the same plot

unrate['MONTH'] = unrate['DATE'].dt.month

fig = plt.figure(figsize=(6,3))
plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red')
plt.plot(unrate[12:24]['MONTH'], unrate[12:24]['VALUE'], c='blue')


# plotting first 5 years on same plot, assigning colors to lines

fig = plt.figure(figsize=(10,6))

for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    colors = ['red', 'blue', 'green', 'orange', 'black']
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i])

# adding legend with color of line and year , assigning to upper left

fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
years = ['1948','1949','1950','1951','1952']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i], label=years[i])
    plt.legend(loc='upper left')

# adding labels and title

plt.title("Monthly Unemployment Trends, 1948-1952")
plt.xlabel("Month, Integer")
plt.ylabel("Unemployment Rate, Percent")

plt.show()
