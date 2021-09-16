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