from collections import OrderedDict
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))
print (new_d)
#OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

for key in new_d:
    print (key, new_d[key])

#apple 4
#banana 3
#orange 2
#pear 1

for key in reversed(new_d):
    print (key, new_d[key])