# displaying current time stamp

import time
import datetime

current_time = time.time()
print (current_time)

# converting a timestamp using the time.gmtime() function with attributes
#tm_year, tm_mon, tm_mday, tm_hour, tm_min


current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour
print (current_hour)

# using datetime.utcnow()


current_datetime = datetime.datetime.utcnow()
current_year = current_datetime.year
current_month = current_datetime.month
print (current_datetime)

# using timedelta class in module datetime


kirks_birthday = datetime.datetime(year=2233, month=3, day=22)
diff = datetime.timedelta(weeks = 15)
before_kirk = kirks_birthday - diff

# using datetime.datetime.strftime() method for more readable date
# mystery_date_formatted_string = 12:00AM on Thursday January 02, 2003,
# mystery_date = 2003-01-02 00:00:00


mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print (mystery_date_formatted_string)


mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print (mystery_date_2)

# using askreddit_2015.csv for following problems
# converting Unix time to float and float to datetime instance using datetime.datetime.fromtimestamp()
# then overwriting original time

for row in posts:
    row[2] = float(row[2])
    row[2] = datetime.datetime.fromtimestamp(row[2])

    print(row[2])

# number of times people posted in march

march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1

# function for posts in given month

def num_posts(num):
    count = 0
    for row in posts:
        if row[2].month == num:
            count += 1
    return count

feb_count = num_posts(2)
aug_count = num_posts(8)
