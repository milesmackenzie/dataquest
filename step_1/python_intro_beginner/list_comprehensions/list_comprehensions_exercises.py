# practice with list comprehensions:

apple_prices = [100, 101, 102, 105]

apple_prices_doubled = [x * 2 for x in apple_prices]
print(apple_prices_doubled)

apple_prices_lowered = [x-100 for x in apple_prices]
print(apple_prices_lowered)

values = [None, 10, 20, 30, None, 50]
checks = []
checks = [x is not None and x>30 for x in values]

print (checks)

# practice with enumerate:


ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for idx, ship in enumerate(ships):
    print(ship)
    print(cars[idx])

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for idx, item in enumerate(things):
    item.append(trees[idx])
print(things)

#exercise continued legislators:

import csv

f = open("legislators.csv", "r")
legislators = list(csv.reader(f))

legislators = legislators[1:]

for row in legislators:
    birthday = row[2]
    birth_year = birthday.split("-")
    try:
        birth_year[0] = int(birth_year[0])
    except Exception:
        birth_year[0] = 0
    row.append(birth_year[0])

last_value = 1

for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]

name_counts = {}
print (legislators[0:10])

for row in legislators:
    if row[3] == "F" and row[7] > 1940:
        name = row[1]
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1


# highest male count name

top_male_names = []
male_name_counts = {}

for item in legislators:
    if item[3] == "M" and item[7] > 1940:
        if item[1] in male_name_counts:
            male_name_counts[item[1]] += 1
        else:
            male_name_counts[item[1]] = 1

highest_male_count = 0

for x, xx in male_name_counts.items():
    if xx > highest_male_count:
        highest_male_count = xx
print(highest_male_count)


for h, hh in male_name_counts.items():
    if hh == 35:
        top_male_names.append(h)
print(top_male_names)
