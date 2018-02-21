# importing math, math as m and all math functions

import math
root = math.sqrt(99)
flr = math.floor(89.9)


import math as m
root = m.sqrt(33)

from math import *
print (sqrt(1001))


a = math.sqrt(pi)
b = math.ceil(pi)
c = math.floor(pi)

print(math.floor(pi))
print(math.pi)
print (b)

# importing csv to read nfl.csv

import csv
n = open("nfl.csv")
nfl_reader = csv.reader(n)
nfl = list(nfl_reader)

print (nfl)

# counting how many times the New England Patriots won

import csv
f = open("nfl.csv", "r")
nfl = list(csv.reader(f))

patriots_wins = 0

for item in nfl:
    if item[2] == "New England Patriots":
        patriots_wins += 1

print (patriots_wins)

# giving win totals for a given team

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins(team):
    count = 0
    for row in nfl:
        if row[2] == team:
            count = count + 1
    return count

cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")

print(falcons_wins)
