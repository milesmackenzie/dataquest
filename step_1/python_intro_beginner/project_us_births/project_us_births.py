# https://github.com/fivethirtyeight/data/blob/master/births/US_births_1994-2003_CDC_NCHS.csv

# year: Year (1994 to 2003).
# month: Month (1 to 12).
# date_of_month: Day number of the month (1 to 31).
# day_of_week: Day of week (1 to 7).
# births: Number of births that day.

f = open("US_births_1994-2003_CDC_NCHS.csv", "r")
csvread = f.read()
data = csvread.split("\n")

# Read csv file

def read_csv(string):
    final_lst = []
    f = open(string, "r")
    csvread = f.read()
    data = csvread.split("\n")
    data.remove(data[0])
    string_list = data
    int_fields = []

    for item in string_list:
        int_fields.append(item.split(","))

    for items in int_fields:
        final_lst.append([int(x) for x in items])

    return (final_lst)

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")

# Births per month function

def month_births(lst_lst):
    data = lst_lst
    births_per_month = {}

    for item in data:
        if item[1] not in births_per_month:
            births_per_month[item[1]] = item[4]
        else:
            births_per_month[item[1]] += item[4]

    return births_per_month

#births per week function

def dow_births(input_lst):
    data = input_lst
    day_of_week = {}
    for item in data:
        if item[3] not in day_of_week:
            day_of_week[item[3]] = item[4]
        else:
            day_of_week[item[3]] += item[4]

    return day_of_week

# births per year function

def year_births(input_lst):
    data = input_lst
    year = {}
    for item in data:
        if item[0] not in year:
            year[item[0]] = item[4]
        else:
            year[item[0]] += item[4]

    return year

# births per month function

def dom_births(input_lst):
    data = input_lst
    day_of_month = {}
    for item in data:
        if item[2] not in day_of_month:
            day_of_month[item[2]] = item[4]
        else:
            day_of_month[item[2]] += item[4]

    return day_of_month

# function to display dictionary of totals for give column

def calc_counts(lst, column):
        data = lst

        if column == 1:
            cdc_year_births = year_births(lst)
            return cdc_year_births
        elif column == 2:
            cdc_month_births= month_births(lst)
            return cdc_month_births
        elif column == 3:
            cdc_dom_births = dom_births(lst)
            return cdc_dom_births
        elif column == 4:
            cdc_dow_births = dow_births(lst)
            return cdc_dow_births
        else:
            return "Column does not exist"


def min_max(dct, mm):
    num = []
    for item in dct:
        num.append(dct[item])
    if mm == "min":
        return min(num)
    if mm == "max":
        return max(num)


# Function to compare birth numbers on saturdays from different years

def compare(lst, year1, year2, day):
    if day == "Monday":
        day = 1
    elif day == "Tuesday":
        day = 2
    elif day == "Wednesday":
        day = 3
    elif day == "Thursday":
        day = 4
    elif day == "Friday":
        day = 5
    elif day == "Saturday":
        day = 6
    elif day == "Sunday":
        day = 7

    total_list_year1 = 0
    total_list_year2 = 0

    for item in lst:
        if year1 == item[0] and day == item[3]:
            total_list_year1 += item[4]
    for item in lst:
        if year2 == item[0] and day == item[3]:
            total_list_year2 += item[4]

    if day == 1:
        day = "Mondays"
    elif day == 2:
        day = "Tuesdays"
    elif day == 3:
        day =  "Wednesdays"
    elif day == 4:
        day = "Thursdays"
    elif day == 5:
        day = "Fridays"
    elif day == 6:
        day = "Saturdays"
    elif day == 7:
        day = "Sundays"

    if total_list_year2 > total_list_year1:
        return ("There were " + str(total_list_year2 - total_list_year1) + " more births on %s in %s than %s in %s" % (day, year2, day, year1))

    if total_list_year2 < total_list_year1:
        return ("There were " + str(total_list_year1 - total_list_year2) + " more births on %s in %s than %s in %s" % (day, year1, day, year2))





print (compare(cdc_list, 1997, 1998, "Saturday"))
