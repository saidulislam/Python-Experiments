from itertools import count

# The count iterator will return evenly spaced values 
# starting with the number you pass in as its start parameter.
for i in count(10):
    if i > 20: 
        break
    else:
        print(i)

print()

from itertools import islice
for i in islice(count(10), 5):
    print(i)

print()

from itertools import cycle
count = 0
for item in cycle('XYZ'):
    if count > 7:
        break
    print(item)
    count += 1


polys = ['triangle', 'square', 'pentagon', 'rectangle']
iterator = cycle(polys)
print (next(iterator))
#'triangle'

print (next(iterator))
#'square'

print (next(iterator))
#'pentagon'

print (next(iterator))
#'rectangle'

print (next(iterator))
#'triangle'

print (next(iterator))
#'square'


from itertools import repeat

# basically, repeat 5 5 times
iterator = repeat(5, 5)
print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 21, in <module>
# print (next(iterator))
#StopIteration: