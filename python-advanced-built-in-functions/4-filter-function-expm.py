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
