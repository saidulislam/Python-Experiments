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
