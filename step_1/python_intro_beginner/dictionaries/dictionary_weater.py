# Count how many times each type of weather occurs in the weather list,
# and store the results in a new dictionary called weather_counts.

weather_counts = {}

for item in weather:
    if item in weather_counts:
        weather_counts[item] += 1
    else:
        weather_counts[item] = 1

print(weather_counts)
