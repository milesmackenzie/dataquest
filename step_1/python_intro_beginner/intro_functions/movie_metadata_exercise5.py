
# Write a summary_statistics() function that will take movie_data
# as input, and output a dictionary that will give useful numbers from the data.

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt
def summary_statistics(input_lst):
    num_japan_films = feature_counter(input_lst,6,"Japan",True)
    num_color_films = feature_counter(input_lst,2,"Color",True)
    num_films_in_english = feature_counter(input_lst,5,"English",True)
    dictionary = {}
    dictionary["japan_films"] = num_japan_films
    dictionary["color_films"] = num_color_films
    dictionary["films_in_english"] = num_films_in_english
    return dictionary

summary = summary_statistics(movie_data)
print (summary)
