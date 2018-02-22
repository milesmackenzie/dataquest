
# Indroducing US gun deaths data

import csv

f = open("guns.csv", "r")
data = list(csv.reader(f))

# removing headers

headers = data[0]
data = data[1:]

print (data[0:10])

# counting gun deaths by year

years = [x[1] for x in data]

year_counts = {}
for item in years:
    if item in year_counts:
        year_counts[item] += 1
    else:
        year_counts[item] = 1

#gun deaths by month and year

import datetime
dates = []
for item in data:
    date = datetime.datetime(year = int(item[1]), month = int(item[2]), day=1)
    dates.append(date)

date_counts = {}

for item in dates:
    if item in date_counts:
        date_counts[item] += 1
    else:
        date_counts[item] = 1

#gun deaths by race and sex

sex_counts = {}
race_counts = {}

for item in data:
    if item[5] in sex_counts:
        sex_counts[item[5]] += 1
    else:
        sex_counts[item[5]] = 1

for item in data:
    if item[7] in race_counts:
        race_counts[item[7]] += 1
    else:
        race_counts[item[7]] = 1

# We've learned that male deaths are approximately
# 6 times more than women. White race has more gun deaths than any other race but knowing
# total counts of population for each race would help better display the data.
# At this points we've looked at counts of male, female and race gun deaths separately.
# We might want to look at the race distribution within females and males, look
# at the intent between females, males and race and explore education level.

#reading in census
# data: [['Id', 'Year', 'Id', 'Sex', 'Id', 'Hispanic Origin', 'Id', 'Id2',
# 'Geography', 'Total', 'Race Alone - White', 'Race Alone - Hispanic',
# 'Race Alone - Black or African American', 'Race Alone - American Indian and Alaska Native',
# 'Race Alone - Asian', 'Race Alone - Native Hawaiian and Other Pacific Islander', 'Two or More Races'],
# ['cen42010', 'April 1, 2010 Census', 'totsex', 'Both Sexes', 'tothisp', 'Total', '0100000US', '', 'United States',
# '308745538', '197318956', '44618105', '40250635', '3739506', '15159516', '674625', '6984195']]


census = [['Id', 'Year', 'Id', 'Sex', 'Id', 'Hispanic Origin', 'Id', 'Id2', 'Geography', 'Total', 'Race Alone - White', 'Race Alone - Hispanic', 'Race Alone - Black or African American', 'Race Alone - American Indian and Alaska Native', 'Race Alone - Asian', 'Race Alone - Native Hawaiian and Other Pacific Islander', 'Two or More Races'], ['cen42010', 'April 1, 2010 Census', 'totsex', 'Both Sexes', 'tothisp', 'Total', '0100000US', '', 'United States', '308745538', '197318956', '44618105', '40250635', '3739506', '15159516', '674625', '6984195']]

# rates of gun deaths per race

mapping = {}
census1 = [item[9:] for item in census]
census1 = census1[0]
count = []

count.append(census[1])
for item in count:
    count = item[9:]

for idx, item in enumerate(census1):
    mapping[item] = count[idx]

keys_counts = {}

for item in data:
    if item[7] in keys_counts:
        keys_counts[item[7]] = 0
    else:
        keys_counts[item[7]] = 0

keys_counts['Asian/Pacific Islander'] = int(mapping['Race Alone - Asian']) + int(mapping['Race Alone - Native Hawaiian and Other Pacific Islander'])
keys_counts["Black"] = int(mapping['Race Alone - Black or African American'])
keys_counts['Hispanic'] = int(mapping['Race Alone - Hispanic'])
keys_counts['Native American/Native Alaskan'] = int(mapping['Race Alone - American Indian and Alaska Native'])
keys_counts['White'] = int(mapping['Race Alone - White'])

race_per_hundredk = {}

for item in race_counts:
    race_per_hundredk[item] = race_counts[item]/keys_counts[item] * 100000

#filtered by intent

intents = [x for x in data if x[3] == 'Homicide']
races = [x[7] for x in intents]

homicide_race_counts = {}

for race in races:
    if race in homicide_race_counts:
        homicide_race_counts[race] += 1
    else:
        homicide_race_counts[race] = 1

for item in homicide_race_counts:
    homicide_race_counts[item] = homicide_race_counts[item]/keys_counts[item] * 100000


# Displayed dictionaries showing number of deaths per 100000 people per
# race and number of homidice deaths per 100000 per race based on total
# populations of race. It would be interesting to look at education level on intent,
# if certain time periods in the year have increased death rates and which intent is increased.

# link between month and homicidal rate

homicides = []
month_deaths = {}

for item in data:
    if item[3] == "Homicide":
        homicides.append(item)

for item in homicides:
    if item[2] not in month_deaths:
        month_deaths[item[2]] = 1
    else:
        month_deaths[item[2]] += 1

# homicide rate by gender total numbers for each gender needed for rate.
# assuming 50/50, total gender for each would be 308745538/2 = 154372769
gender_homicide = {}

for item in homicides:
    if item[5] not in gender_homicide:
        gender_homicide[item[5]] = 1
    else:
        gender_homicide[item[5]] += 1

for item in gender_homicide:
    gender_homicide[item] = (gender_homicide[item]/154372769) * 100000
