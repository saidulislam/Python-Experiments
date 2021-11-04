from functools import singledispatch


@singledispatch
def add(a, b):
    # This function is our catch-all function and will 
    # only get called if none of the other decorated functions 
    # handle the type passed.
    #
    # You will note that we currently handle integers, strings and 
    # lists as the first argument. If we were to call our add function 
    # with something else, such as a dictionary, then it would raise 
    # a NotImplementedError.
    raise NotImplementedError('Unsupported type')


@add.register(int)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(str)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(list)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


if __name__ == '__main__':
    add(1, 2)
    add('Python', 'Programming')
    add([1, 2, 3], [5, 6, 7])