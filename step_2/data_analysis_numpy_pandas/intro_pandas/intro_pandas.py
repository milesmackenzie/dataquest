# reading food_info.csv with pandas.read_csv(), printing type

import pandas

food_info = pandas.read_csv("food_info.csv")
print(type(food_info))

# using .head() to print out given number of rows and .shape to find dimensions

print(food_info.head(3))
dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)

first_twenty = food_info.head(20)

# using .loc() to print given row or multiple rows

hundredth_row = food_info.loc[99]
last_rows = food_info.loc[8613:8618]

# accessing column by name using bracket notation

saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]

# accessing multiple columns in order

selenium_thiamin = food_info[["Selenium_(mcg)", "Thiamin_(mg)"]]

# Selecting and displaying only the columns that use grams for
# measurement (end with "(g)") using .tolist() and .endswith() function calls

lst = food_info.columns.tolist()
gram_columns = []

for item in lst:
    if item.endswith("(g)"):
        gram_columns.append(item)
gram_df = food_info[gram_columns]
print(gram_df.head(3))
