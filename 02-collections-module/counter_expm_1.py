from collections import Counter
print (Counter('superfluous'))
#Counter({'u': 3, 's': 2, 'e': 1, 'l': 1, 'f': 1, 'o': 1, 'r': 1, 'p': 1})

counter = Counter('superfluous')
print (counter['u'])
#3

print (list(counter.elements()))
#['u', 'u', 'u', 'o', 'p', 'e', 'f', 'l', 'r', 's', 's']

print(counter.most_common(2))
#[('u', 3), ('s', 2)]

counter_one = Counter('superfluous')
print (counter_one)
#Counter({'u': 3, 's': 2, 'l': 1, 'r': 1, 'e': 1, 'o': 1, 'p': 1, 'f': 1})

counter_two = Counter('super')
print(counter_one.subtract(counter_two))
#None

# If you look carefully at the output at the end, you will notice the that 
# number of letters for five of the items has been decremented by one
print(counter_one)
#Counter({'u': 2, 'l': 1, 'o': 1, 's': 1, 'f': 1, 'r': 0, 'e': 0, 'p': 0})