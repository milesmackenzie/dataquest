def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(input_lst,index,string,header_row=False):

    num_of_us_movies = 0
    if header_row == True:
        input_lst == input_lst[1:len(input_lst)]
    for item in input_lst:
        if item[index] == string:
            num_of_us_movies += 1
    return num_of_us_movies

num_of_us_movies = feature_counter(movie_data,6,"USA",True)
print (num_of_us_movies)

# Write a function named feature_counter() that combines the logic of the index_equals_str() and counter() functions.
# Use this to find out how many of the movies were made in USA, and store the value in num_of_us_movies.
