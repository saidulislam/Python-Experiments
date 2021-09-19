friends = ['Abby', 'Aaron', 'John', 'Debbie', 'Rick', 'Austin']

# to show example use of map
lowercase_friends = map(lambda x: x.lower(), friends) # x.lower() will be executed for each item in friends
l_friends = [f for f in lowercase_friends]
print(l_friends)

# you can also use generator comprehension like the following
l_friends = (f.lower() for f in friends)
print([f for f in l_friends])

# you can also do
l_friends = [f.lower() for f in friends]
print(l_friends)


"""
map is a function that allows us to call some other function on every item in an iterable. 
And what are functions? They're just a means of defining some action we want to perform in a reusable way. 
In other words, map is a way of performing some action for every item in an iterable, just like a comprehension.

Let's say I want to cube every number in a list of numbers. We can use map like so:

"""

def cube(number):
	return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

for number in cubed_numbers:
	print(number)


""" 
Since they're iterable, we can also unpack them using *
"""

def cube(number):
	return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(cube, numbers)

print(*cubed_numbers, sep=", ")

""" We can also convert them to a normal collection if we like """
def cube(number):
	return number ** 3

numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(cube, numbers))
print(cubed_numbers)


# map with multiple iterables
# One of the really nice things about map is that is can handle several iterables at once.
def add(a, b):
	return a + b

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19


# map with lambda expressions
numbers = [1, 2, 3, 4, 5]
cubed_numbers = map(lambda number: number ** 3, numbers)
print(*cubed_numbers)


# We could have used a lambda expression here like this:

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(lambda a, b: a + b, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19

# btw... operator has an add function ready to go, so we don't have to define it ourselves.
from operator import add

odds = [1, 3, 5, 7, 9]
evens = [2, 4, 6, 8, 10]

totals = map(add, odds, evens)
print(*totals, sep=", ")  # 3, 7, 11, 15, 19


# Another really useful function in operator is methodcaller. methodcaller allows us to 
# easily define a function that calls a method for us. We just have to provide the method name as a string.
from operator import methodcaller

names = ["tom", "richard", "harold"]
title_names = map(methodcaller("title"), names)
print(*title_names)