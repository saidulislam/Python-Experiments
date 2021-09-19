"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

## Counter
"""
Allows us to count things. Give it a iterable or a mapping (such as a dict) and it will turn into a counter of elements.
"""

from collections import Counter

temps = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]
temps_counter = Counter(temps)

# how many times 14.5 are there
print(temps_counter[14.5])


## defaultdict
"""
The `defaultdict` never raises a `KeyError`. Instead, it returns the value returned 
by the function specified when the object was instantiated.
"""

# alma_maters = {}

# for coworker in coworkers:
#     if coworker[0] in alma_maters:
#         alma_maters[coworker[0]] = []
#     alma_maters[coworker[0]].append(coworker[1])

from collections import defaultdict

coworkers = [('John', 'MIT'), ('Rick', 'Oxford'), ('Dan', 'OSU'), ('Ellie', 'MU')]

coworker_alma_maters = defaultdict(list)  # list is a function, returns []

for coworker, place in coworkers:
    coworker_alma_maters[coworker].append(place)

print(coworker_alma_maters['John'])
print(coworker_alma_maters['Anne'])  # []
print("\n")


"""
When you need a dictionary and all keys of that dictionary should be associated with an initial value, use `defaultdict`!

Another example is to initialise places where coworkers work:
"""

from collections import defaultdict

my_company = 'AWESOME TEK'

coworkers = ['Jen', 'Li', 'Charlie', 'Ray']
other_coworkers = [('Rick', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies['Jen'])  # AWESOME TEK
print(coworker_companies['Rick'])  # Apple Inc.


"""
If you want to change the default value in a `defaultdict`, just change its `default_factory` property:
"""

from collections import defaultdict

int_dict = defaultdict(int)

int_dict['first'] += 1
print(int_dict['first'])  # 1

int_dict.default_factory = list
int_dict['second'].append('Jack')
print(int_dict['second'])  # ['Jack']

int_dict.default_factory = None  # this is back to being a "normal dictionary"


## OrderedDict

from collections import OrderedDict

o = OrderedDict()
o['John'] = 6
o['Dan'] = 10
o['Brent'] = 3
print("\n")
print(o)  # keys are always in the order in which they were inserted

o.move_to_end('John')
o.move_to_end('Dan', last=False)

print(o)

o.popitem()

print(o)


## namedtuple
"""
A namedtuple is another object that we can use like a tuple, where each of the elements of the tuple has a name. In addition, the tuple itself also has a name.

It improves on tuples by making more explicit what it means.

Take this as an example using normal tuples:
"""

account = ('checking', 1850.90)

print(account[0])  # name
print(account[1])  # balance


"""
Or, the explicitness of `namedtuple`:
"""

from collections import namedtuple

Account = namedtuple('Account', ['name', 'balance'])
account = Account('checking', 1850.90)
print(account.name)
print(account.balance)

"""
I like to think of it very much like defining a class (where `Account` is the class or the type). However, remember it’s not quite the same, and a `namedtuple` is still a tuple after all.

You can do things like these:
"""

name, balance = account  # tuple destructuring
print(name)
print(balance)

Account('checking', balance=1850.90)  # use positional or named arguments
Account._make(('checking', 1850.90))


accounts = [
    ('checking', 1850.90),
    ('savings', 3658.00),
    ('credit', -450.00)
]

account_tuples = map(Account._make, accounts)
account._asdict()  # returns an OrderedDict representing the tuple

print(accounts)

## Deque
"""
`deque` stands for “Double-ended queue”.

In a `deque`, we can push elements at the start or the end, and we can also remove 
elements from the start or the end.

It is very efficient, performing very well, and also it’s thread-safe 

it’s like a list on which you do operations like a list:
"""

from collections import deque

friends = deque(('John', 'Dan', 'Jen', 'Anna'))
friends.append('Jose') # goes at the end
friends.appendleft('Anthony') # goes at the beginning 

print(friends)

friends.pop() # remove Jose, the last item
print(friends)

friends.popleft() # remove Anthony, the first item
print(friends)

