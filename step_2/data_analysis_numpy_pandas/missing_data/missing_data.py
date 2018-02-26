# reading in titanic_survival.csv

import pandas as pd
import numpy as np

titanic_survival = pd.read_csv("titanic_survival.csv")

age = titanic_survival["age"]


# using .isnull() function to determine if a value is None or NaN (not a number)
# giving True and False bools

age_is_null = pd.isnull(age)
age_null_true = age[age_is_null]
age_null_count = len(age_null_true)
#
# print (age_null_count)

# determining average age without null values

age_is_null = pd.isnull(titanic_survival["age"])
without_null = titanic_survival["age"][age_is_null == False]
correct_mean_age = sum(without_null)/len(without_null)

# print (correct_mean_age)

# using .mean() function to calculate mean without eliminating nulls
# pandas method automatically filters

correct_mean_age = titanic_survival["age"].mean()
correct_mean_fare = titanic_survival["fare"].mean()

# finding average fares for passengers in each class

passenger_classes = [1, 2, 3]
fares_by_class = {}

for num in passenger_classes:
    class_rows = titanic_survival[titanic_survival["pclass"] == num]
    fares = class_rows["fare"]
    fares_by_class[num] = fares.mean()


# using the DataFrame.pivot_table() function and aggfunc=np.mean to
# calculate average ages in different classes

passenger_age = titanic_survival.pivot_table(index="pclass", values="age", aggfunc=np.mean)
# print (passenger_age)

# passing a list through the values parameter to make calculations on
# multiple columns at the same time

port_stats = titanic_survival.pivot_table(index="embarked", values=["fare", "survived"], aggfunc=np.sum)


# using DataFrame.dropna() to drop any rows missing data, using axis=0 (rows) and
# axis=1 (colums)

drop_na_rows = titanic_survival.dropna(axis=0)
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0, subset=["age","sex"])

# new_titanic_survival sorted by age. using .iloc[] and .loc[]

first_ten_rows = new_titanic_survival.iloc[0:10]
row_position_fifth = new_titanic_survival.iloc[4]
row_index_25 = new_titanic_survival.loc[25]


# indexing columns using both .iloc[] and .loc[]

row_index_1100_age = new_titanic_survival.loc[1100, "age"]
print(row_index_1100_age)
row_index_25_survived = new_titanic_survival.loc[25, "survived"]
five_rows_three_cols = new_titanic_survival.iloc[0:5,0:3]

# creating new index from 0, dropping old index

titanic_reindexed = new_titanic_survival.reset_index(drop=True)
# print (titanic_reindexed.iloc[0:5,0:3])

# function for counting null counts for each column and using .apply()

def count_null(column):
    null = pd.isnull(column)
    null_2 = column[null]
    return len(null_2)

column_null_count = titanic_survival.apply(count_null)
print (column_null_count)

# function for determining if passenger was a minor or adult

def check_age(row):
    if row["age"] < 18:
        return "minor"
    elif pd.isnull(row["age"]):
        return "unknown"
    else:
        return "adult"

age_labels = titanic_survival.apply(check_age, axis=1)

# probability of survival for each age group using pivot_table

age_group_survival = titanic_survival.pivot_table(index="age_labels", values="survived", aggfunc=np.mean)

print (age_group_survival)
