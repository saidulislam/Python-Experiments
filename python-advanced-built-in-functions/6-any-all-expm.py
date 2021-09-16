"""
The two functions we’ll be talking about are very straightforward, but in some cases can be really useful.

The `any()` function takes an iterable and returns `True` if any of the elements in it evaluate to `True`

The `all()` function returns `True` if all the elements evaluate to `True`.

Here’s an example of when it might be useful.
"""

friends = [
  {
    'name': 'John',
    'location': 'Washington, D.C.'
  },
  {
    'name': 'Bill',
    'location': 'San Francisco'
  },
  {
    'name': 'Ben',
    'location': 'San Francisco'
  },
  {
    'name': 'Carlisle',
    'location': 'San Francisco'
  },
]

your_location = input('What is your current location? ')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):
  print('You are not alone!')
else:
  print('No friends nearby')


"""
Here the contents of `friends_nearby` is a list of dictionaries—not `True` or `False`.

However, all values in Python can evaluate to either `True` or `False` if forced to.

Some values always evaluate to `False`:

* `0`
* `None`
* `[]`
* `()`
* `{}`
* `False`

All other values evaluate to `True`—so if we have a dictionary with values in it, that evaluates to `True` and the `any()` function will then return `True`.

However, if we pass it an empty list, we get `False`.
"""

my_awesome_list = [True, True, False]
if all(my_awesome_list):
  print("all true")
else:
  print("not all true")