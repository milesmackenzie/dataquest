# Append any names in planet_names that are longer than 5 characters to long_names. Otherwise, append the names to short_names.

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []

for item in planet_names:
    if len(item) > 5:
        long_names.append(item)
    else:
        short_names.append(item)

print (short_names)
print (long_names)
