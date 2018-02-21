# data: https://github.com/fivethirtyeight/data/blob/master/nfl-suspensions/nfl-suspensions-data.csv

import csv

f = open("nfl-suspensions-data.csv", "r")
nfl_suspensions = list(csv.reader(f))
nfl_suspensions = nfl_suspensions[1:] 

years = {}

for lst in nfl_suspensions:
    if lst[5] in years:
        years[lst[5]] += 1
    else:
        years[lst[5]] = 1


print (years)
print (nfl_suspensions[4])

unique_teams = set([x[1] for x in nfl_suspensions])
print (unique_teams)

unique_games = set([x[2] for x in nfl_suspensions])
print (unique_games)

# Create a Suspension instance using the third row
# in nfl_suspensions, and assign it to the variable third_suspension.

class Suspension():
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        self.year = row[5]

third_suspension = Suspension(nfl_suspensions[2])

# Instead of assigning the value at index 5 to the year property directly, use a try except block that:
# Tries to cast the value at index 5 to an integer
# If an exception is thrown, assign the value 0 to the year property instead
# Create a method called get_year() that returns the year value for that Suspension instance.
# Create a Suspension instance using the 23rd row, and assign it to missing_year.
# Use the get_year() method to assign the year of the missing_year suspension instance to twenty_third_year.

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0

    def get_year(self):
        return(self.year)


missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()
print(twenty_third_year)
