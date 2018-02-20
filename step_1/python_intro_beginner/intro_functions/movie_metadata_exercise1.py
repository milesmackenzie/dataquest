#Write a function, with a definition, name, argument(s), body and return value, that returns a list containing the names of the movies in movie_data.
#This function is expected to behave similar to first_elt(), but for multiple lists.

def first_elts(input_lst):
    movie = []

    for item in input_lst:
        movie.append(item[0])
    return movie

movie_names = first_elts(movie_data)
print(movie_names[0:5])
