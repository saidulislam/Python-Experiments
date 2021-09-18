def mul(*args):
    print("args[0] : ", args[0])
    print("args[1] : ", args[1])
    return (args[0]*args[1])

num = mul(3, 9, 7)
print(num)


def multigreet(*args):
    for item in args:
        print(f"Hello {item}!")

multigreet("John", "Conner", "Ryan", "Tim")

print("\n\n")

# *args has to be the last argument
def multigreet2(msg, *args):
    for item in args:
        print(f"{msg} {item}!")

multigreet2("Hey", "John", "Conner", "Ryan", "Tim")


def print_family_info(**kwargs):
    family = {}
    for key, value in kwargs.items():
        family[key] = value

    print(family)

print("\n\n")
print_family_info(mom="Jane", dad="John", child1="Rick", child2="Ellie")
print("\n\n")

# more use of *args
def print_movie(*args):
    for value in args:
        print(value)


movie = {
	"title": "The Matrix",
	"director": "Wachowski",
	"year": 1999
}


print_movie(*movie.values())
print("\n\n")

# more use of **kwargs
def print_movie(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")


movie = {
	"title": "The Matrix",
	"director": "Wachowski",
	"year": 1999
}

print_movie(**movie)
print("\n\n")


# **kwargs can give us more flexibility 
# when it comes to collecting unassigned keyword arguments, 
# and not only those coming from a dictionary.

# For example, we could do this:
def print_movie(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")


movie = {
	"title": "The Matrix",
	"director": "Wachowski",
	"year": 1999
}


print_movie(studio="Warner Bros", **movie)
print("\n\n")


# There are plenty more uses for a technique like this, including merging dictionaries, 
# and saving us a lot of typing when using format

# for example, instead of the following
def show_books(books):
	# Adds an empty line before the output
	print()

	for book in books:
		print(f"{book['title']}, by {book['author']} ({book['year']})")

	print()


# you can do something like the following
def show_books(books):
	# Adds an empty line before the output
	print()

	for book in books:
		print("{title}, by {author} ({year})".format(**book))

	print()


# One of the nice things about this approach is that 
# we can define the template elsewhere, which also means 
# we can refer to it in multiple places in our code.

book_template = "{title}, by {author} ({year})"

def show_books(books):
	# Adds an empty line before the output
	print()

	for book in books:
		print(book_template.format(**book))

	print()