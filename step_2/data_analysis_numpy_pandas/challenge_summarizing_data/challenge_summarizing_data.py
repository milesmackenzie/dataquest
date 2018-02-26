import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")

print (all_ages[0:5])
print(recent_grads[0:5])

# function for determining how many graduates majored in each major

def totals(data):
    aa_cat_counts = {}
    rg_cat_counts = {}
    for item in data['Major_category'].unique():
        major = data[data['Major_category'] == item]
        aa_cat_counts[item] = major["Total"].sum()
    return aa_cat_counts

aa_cat_counts = totals(all_ages)
rg_cat_counts = totals(recent_grads)

print(aa_cat_counts)

# percent of recent grads who work low wage jobs

low_wage_proportion = (recent_grads["Low_wage_jobs"].sum())/(recent_grads["Total"].sum())

# counting rows where unemployment rate is lower for recent grads when compared
# to everyone

majors = recent_grads['Major'].unique()
rg_lower_count = 0

for item in majors:
    rg = recent_grads[recent_grads['Major'] == item]
    aa = all_ages[all_ages['Major'] == item]
    rg_rate = rg.iloc[0]['Unemployment_rate']
    aa_rate = aa.iloc[0]['Unemployment_rate']
    if rg_rate < aa_rate:
        rg_lower_count += 1
print (rg_lower_count)
    
