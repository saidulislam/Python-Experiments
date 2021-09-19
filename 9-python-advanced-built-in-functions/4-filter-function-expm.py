friends = ['Abby', 'Aaron', 'John', 'Debbie', 'Rick', 'Austin']
friends_starting_a = filter(lambda x: x.startswith('A'), friends)

# friends_starting_a is now generator obj

# you can do something like the following
# print(next(friends_starting_a))

# Or, you can do something like the following
print([f for f in friends_starting_a])


# all of the above can also be done the following way
# without the filter
starts_with_a = [a for a in friends if a.startswith('A')]
print(starts_with_a)

# start_with_a can be a generator obj like the following
starts_with_a = (a for a in friends if a.startswith('A'))
print([f for f in starts_with_a])


# Much like map, filter calls a function (known as a predicate) 
# for every item in an iterable, and it discards any values for which that function returns a falsy value.

# A predicate is a function that accepts some value as an argument and returns either True or False.

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(lambda number: number % 2 == 0, numbers)

print(*even_numbers)

# of course, you can also call a function in filter
def is_even(number):
	return number % 2 == 0

numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_numbers = filter(is_even, numbers)

print(*even_numbers)

# Using None with filter
# Instead of passing in a function to filter, it's possible to use the value None. 
# This tells filter that we want to use the truth values of the values directly, instead of performing 
# some kind of comparison, or calculating something.

# In this case, filter will keep all truthy values from the original iterable, and all falsy values 
# will be discarded.

values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)

print(*truthy_values, sep=", ")  # Hello, 435, -4.2

