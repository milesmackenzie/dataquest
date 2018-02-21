# beginning classes

class Dataset:
    def __init__(self):
        self.type = "csv"

dataset = Dataset()

print(dataset.type)

# reading data in classes

import csv

class Dataset:
    def __init__(self, data):
        self.data = data

f = open("nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data

#printing given number of rows

class Dataset:
    def __init__(self, data):
        self.data = data

    def print_data(self, num_rows):
        print(self.data[:num_rows])

nfl_dataset = Dataset(nfl_data)

print (nfl_dataset.print_data(5))

# removing header rows

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]


nfl_dataset = Dataset(nfl_data)

nfl_header = nfl_dataset.header
nfl_data = nfl_dataset.data

print(nfl_data[0:5])



# Add a method named column that takes in a label argument, finds the index of the header, and returns a list of the column data.
# If the label is not in the header, you should return None.
# Create a variable called year_column and set it to the return value of column('year').
# Create a variable called player_column and set it to the return value of column('player').


class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    def column(self, label):
        if label not in self.header:
            return None
        index = 0
        for idx, item in enumerate(self.header):

            if label == item:
                index = idx

        column = []
        for row in self.data:
            column.append(row[index])
        return column



nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')


#adding method count_unique to class

# Add a method to the Dataset class called count_unique() that takes in a label arguments.
# Get the unique set of items from the column() method and return the total count.
# Use the instance method to assign the number of unique term values of year to total_years.

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    def column(self, label):
        if label not in self.header:
            return None

        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx

        column = []
        for row in self.data:
            column.append(row[index])
        return column
    def count_unique(self, label):
        row = set(self.column(label))
        count = len(row)
        return count



nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')


# Add a method to the Dataset class called __str__()
#
# Convert the first 10 rows of self.data to a string and set it as the return value.
# Create an instance of the class called nfl_dataset and call print on it.

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]

    # Add the special method here

    def column(self, label):
        if label not in self.header:
            return None

        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx

        column = []
        for row in self.data:
            column.append(row[index])
        return column


    def count_unique(self, label):
        unique_results = set(self.column(label))
        count = len(unique_results)
        return count

    def __str__(self):
        return str(self.data[0:10])

nfl_dataset = Dataset(nfl_data)
print (nfl_dataset)
