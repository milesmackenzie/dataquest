# Create a list of integers named int_crime_rates that contains just the crime rates - as integers - from the list rows.

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])

int_crime_rates = []
new_list = []

for item in rows:
    item = item.split(',')
    new_list.append(item)

for item in new_list:
    int_crime_rates.append(item[1])

int_crime_rates = [int(x) for x in int_crime_rates]

print (int_crime_rates)
