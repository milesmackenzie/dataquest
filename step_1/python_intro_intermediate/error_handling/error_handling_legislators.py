import csv

f = open("legislators.csv", "r")
legislators = list(csv.reader(f))

for row in legislators:
    if row[3] == "":
        row[3] = "M"

gender = []
for item in legislators:
    gender.append(item[3])
gender = set(gender)
print (gender)


party = []
for item in legislators:
    party.append(item[6])
party = set(party)
print (party)


birth_years = []
for row in legislators:
    parts = row[2].split("-")
    birth_years.append(parts[0])
print (birth_years[0:20])


converted_years = []
for year in birth_years:
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)


for row in legislators:
    birthday = row[2]
    birth_year = birthday.split("-")
    try:
        birth_year[0] = int(birth_year[0])
    except Exception:
        birth_year[0] = 0
    row.append(birth_year[0])

# changing all "" values in the year to the year of the legislator before

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    last_value = row[7]
    print(last_value)
