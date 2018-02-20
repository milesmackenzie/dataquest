# Write a function index_equals_str() that takes in three arguments: a list, an index and a string, and checks whether that index of the list is equal to that string.
# Call the function with a different order of the inputs, using named arguments.
# Call the function on wonder_woman to check whether or not it is a movie in color, store it in wonder_woman_in_color, and print the value.

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False

def index_equals_str(lst, idx, string):
    if lst[idx] == string:
        return True
    else:
        return False
wonder_woman_in_color = index_equals_str(wonder_woman,2,"Color")
print (wonder_woman_in_color)
