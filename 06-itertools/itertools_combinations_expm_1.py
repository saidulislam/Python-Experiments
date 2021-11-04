from itertools import combinations

print (list(combinations('WXYZ', 2)))
#[('W', 'X'), ('W', 'Y'), ('W', 'Z'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]


for item in combinations('WXYZ', 2):
    print(''.join(item))

#WX
#WY
#WZ
#XY
#XZ
#YZ


# The combinations_with_replacement with iterator is 
# very similar to combinations. The only difference is 
# that it will actually create combinations where elements 
# do repeat.
from itertools import combinations_with_replacement

for item in combinations_with_replacement('WXYZ', 2):
    print(''.join(item))

#WW
#WX
#WY
#WZ
#XX
#XY
#XZ
#YY
#YZ
#ZZ


# for creating Cartesian products from a series of input iterables
from itertools import product
arrays = [(-1,1), (-3,3), (-5,5)]
cp = list(product(*arrays))
print (cp)
#[(-1, -3, -5),
# (-1, -3, 5),
# (-1, 3, -5),
# (-1, 3, 5),
# (1, -3, -5),
# (1, -3, 5),
# (1, 3, -5),
# (1, 3, 5)]

