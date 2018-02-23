# using np.array to produce arrays and .shape to produce tuples

import numpy as np

vector = np.array([10, 20, 30])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
vector_shape = vector.shape
matrix_shape = matrix.shape

# reading data sets w/ numpy.genfromtxt() function producing
# type <class 'numpy.ndarray'>

import numpy

world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",")
print (type(world_alcohol))

# using .dtype to show float64 for data type

world_alcohol_dtype = world_alcohol.dtype
print (world_alcohol_dtype)

# reading in data as dtype U75 (75 byte unicode data type), skipping the header and
# setting delimiter to ","

world_alcohol = numpy.genfromtxt("world_alcohol.csv", dtype="U75", skip_header=1, delimiter=",")
print (world_alcohol)

# indexing numpy arrays

uruguay_other_1986 = world_alcohol[1,4]
third_country = world_alcohol[2,2]

# value slicing on numpy arrays

countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]

# selecting one whole demension and a slice of another in a matrix

first_two_columns = world_alcohol[0:,0:2]
first_ten_years = world_alcohol[0:10,0]
first_ten_rows = world_alcohol[0:10,:]
