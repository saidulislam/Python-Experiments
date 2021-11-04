from itertools import permutations

# Much like the combinations function, 
# permutations are emitted in lexicographic sort order

for item in permutations('WXYZ', 2):
    print(''.join(item))

#WX
#WY
#WZ
#XW
#XY
#XZ
#YW
#YX
#YZ
#ZW
#ZX
#ZY