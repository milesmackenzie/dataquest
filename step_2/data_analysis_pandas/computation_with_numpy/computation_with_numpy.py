# reading in world_alcohol.csv with .genfromtxt() with dtype U75, skipping
# header and assigning delimiter to ","

import numpy

world_alcohol = numpy.genfromtxt("world_alcohol.csv", dtype="U75", skip_header=1, delimiter=",")
print (world_alcohol)


# making comparisons accross array

countries_canada = world_alcohol[:,2] == "Canada"
years_1984 = world_alcohol[:,0] == "1984"

# comparing third column with algeria, selecting each row where algeria as
# the country is true and assigning to country_algeria

country_is_algeria = world_alcohol[:,2] == "Algeria"
country_algeria = world_alcohol[country_is_algeria,:]

# selecting rows where column == 1986 and country == Algeria

is_algeria_and_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Algeria")
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

# replacing columns in arrays

replace_date = world_alcohol[:,0] == "1986"
world_alcohol[replace_date, 0] = "2014"

replace_wine = world_alcohol[:,3] == "Wine"
world_alcohol[replace_wine, 3] = "Grog"

print (world_alcohol)

# replacing empty colums "" with "0"

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty, 4] = '0'

# converting the 5th column of world_alcohol to float using .astype

alcohol_consumption = world_alcohol[:,4].astype(float)

# computing sum and mean for columns in alcohol consumption

total_alcohol = alcohol_consumption.sum(axis=0)
average_alcohol = alcohol_consumption.mean(axis=0)

# creat matrix containing rows with 1986 and "Canada". Then extract the 5th
# column, replacing any "" with "0", converting to float() and summing the total.


canada_1986 = (world_alcohol[:,0] == "1986") & (world_alcohol[:,2] == "Canada")

rows_with_canada_1986 = world_alcohol[canada_1986,:]
canada_alcohol = rows_with_canada_1986[:,4]
empty_strings = canada_alcohol == ""
canada_alcohol[empty_strings] = "0"
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()


# finding alcohol totals for all countries in matrix

countries = ['Sierra Leone', 'Namibia', 'Hungary', 'Brunei Darussalam', 'Germany', 'Pakistan', 'Liberia', 'Poland', 'Cyprus', 'Canada', 'Morocco', 'Greece', 'Israel', 'Egypt', 'New Zealand', 'Kiribati', 'Nigeria', 'Ghana', 'Algeria',
'Indonesia', 'Bangladesh', 'Seychelles', 'China', 'Netherlands', 'Belarus', 'Cambodia', 'Saint Kitts and Nevis', 'Lebanon', 'Slovakia', 'Norway', 'Thailand', 'Venezuela (Bolivarian Republic of)', 'Belize', 'Jamaica', 'Sao Tome and Principe', 'Trinidad and Tobago', "Cte d'Ivoire", 'Slovenia', 'Panama', 'South Africa', 'Republic of Korea', 'Equatorial Guinea', 'Swaziland', 'Ethiopia',
'Latvia', 'Samoa', 'Yemen', 'Bhutan', 'Libya', 'Bolivia (Plurinational State of)', 'Tunisia', 'Australia', 'France', "Democratic People's Republic of Korea", 'Rwanda', 'Ecuador', 'Botswana', 'Zambia', 'Senegal', 'Somalia', 'Cabo Verde', 'Fiji', 'Lesotho', 'Burundi', 'Mali', 'Guyana', 'Jordan', 'Chad', 'United Kingdom of Great Britain and Northern Ireland',
'Burkina Faso', 'Kuwait', 'Qatar', 'Solomon Islands', 'Romania', 'Togo', 'Vanuatu', 'Nepal', 'Antigua and Barbuda', 'Micronesia (Federated States of)', 'Portugal', 'Belgium', 'Bulgaria', 'United Republic of Tanzania', 'Saint Lucia', 'Niger', 'Iraq', 'Malaysia', 'Cuba', 'Syrian Arab Republic', 'Iceland', 'Honduras', 'Kenya', 'Mauritania', 'Austria',
'Madagascar', 'Mongolia', 'Haiti', 'Bahrain', 'Czech Republic', 'Spain', 'Viet Nam', 'Dominican Republic', 'Eritrea', 'Albania', 'Guinea-Bissau', 'El Salvador', 'Italy', 'Chile', 'Russian Federation', 'Oman', 'Sudan', 'Cameroon', 'Peru', 'Mozambique', 'Denmark', 'Bahamas', 'Comoros', 'Brazil', 'Japan',
'Iran (Islamic Republic of)', 'Lithuania', 'Ireland', 'Turkey', 'Kyrgyzstan', 'Gabon', 'Costa Rica', 'Uganda', 'Mexico', 'Congo', 'Guatemala', 'Luxembourg', 'Central African Republic', 'Suriname', 'Malawi', 'Guinea', 'Myanmar', 'Democratic Republic of the Congo', 'Malta', 'Djibouti', "Lao People's Democratic Republic", 'Mauritius', 'Sweden', 'India', 'Argentina',
'Switzerland', 'Finland', 'Zimbabwe', 'Papua New Guinea', 'Paraguay', 'Singapore', 'Afghanistan', 'Saudi Arabia', 'Angola', 'Sri Lanka', 'Ukraine', 'Philippines', 'Nicaragua', 'Uruguay', 'Gambia', 'Colombia', 'Benin', 'United States of America', 'Croatia', 'United Arab Emirates']

totals = {}

for item in countries:
    totals[item] = 0

for item in countries:
    year = world_alcohol[:,0] == "1989"
    rows_with_year = world_alcohol[year,:]
    empty_string = rows_with_year[:,4] == '0'
    rows_with_year[empty_string, 4] = "0"
    country = rows_with_year[:,2] == item
    country_consumption = rows_with_year[country,:]
    alcohol = country_consumption[:,4]
    alcohol = alcohol.astype(float)
    totals[item] = alcohol.sum()
print (totals)

# finding country with highest alcohol consumption

highest_value = 0
highest_key = None

for item in totals:
    if totals[item] > highest_value:
        highest_value = totals[item]
        highest_key = item
print (highest_key)
print (highest_value)
