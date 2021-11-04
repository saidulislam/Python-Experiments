from functools import partial
def add(x, y):
    print(x, y)
    return x + y

# send one parameter to the function right now
p_add = partial(add, 2)
# once you have the next parameter ready to send
# basically, send it later
print(p_add(4))
#6