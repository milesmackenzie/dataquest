import csv

f = open("askreddit_2015.csv", "r")
posts_with_header = list(csv.reader(f))

posts = posts_with_header[1:]

# using re module to count occurances of phrase

import re

of_reddit_count_old = 0
for row in posts:
    if re.search("of Reddit", row[0]) is not None:
        of_reddit_count_old += 1

of_reddit_count = 0

for x in posts:
    if re.search("of [rR]eddit", x[0]) is not None:
        of_reddit_count += 1

# searching for Serious and seriois questions in reddit data

import re

serious_count_old = 0
for row in posts:
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count_old += 1

serious_count = 0
for row in posts:
    if re.search("\[[sS]erious\]", row[0]) is not None:
        serious_count += 1

# using square bracket notation to escape "[", "]", ")", "(" with backlash

import re

serious_count_old = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count_old += 1

serious_count = 0
for row in posts:
    if re.search("[\[\(][Ss]erious[\]\)]", row[0]) is not None:
        serious_count += 1



# counting serious statement at start, end and combined

import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0

for x in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]", x[0]) is not None:
        serious_start_count += 1

for x in posts:
    if re.search("[\[\(][Ss]erious[\]\)]$", x[0]) is not None:
        serious_end_count += 1

for x in posts:
    if re.search("^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$", x[0]) is not None:
        serious_count_final += 1


# replacing different forms of "serious" w/ "[Serious]" using re.sub()

import re

for row in posts:
    row[0] = re.sub("[\[\(][Ss]erious[\]\)]", "[Serious]", row[0])


# finding all strings with years in them (determined by numbers between 1000-2999)
# data: ['War of 1812', 'There are 5280 feet to a mile', 'Happy New Year 2016!']

import re

year_strings = []

for string in strings:
    if re.search("[1-2][0-9]{3}", string) is not None:
        year_strings.append(string)
print (year_strings)


# finding all years in strings
# data: 2015 was a good year, but 2016 will be better!

import re

for string in strings:
    years = re.findall("[1-2][0-9]{3}", years_string)
