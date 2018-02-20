#Write a function named is_usa() that checks whether or not a movie was made in the United States.

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(inputs):
    if inputs[-2] == "USA":
        return True
    else:
        return False
wonder_woman_usa = is_usa(wonder_woman)
print(wonder_woman_usa)
