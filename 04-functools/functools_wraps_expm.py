# import functools_wraps_expm
from functools import wraps

def another_function(func):
    """
    A function that accepts another function
    """

    @wraps(func)
    def wrapper():
        """
        A wrapping function
        """
        val = "The result of %s is %s" % (func(),
                                          eval(func())
                                          )
        return val
    return wrapper


@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"


if __name__ == "__main__":
    print(a_function.__name__)
    print(a_function.__doc__)
 
# without the wraps 
#     help(functools_wraps_expm)
#     '''
# $ functools_wraps_expm.py
# Help on module functools_wraps_expm:

# NAME
#     functools_wraps_expm

# FUNCTIONS
#     a_function = wrapper()
#         A wrapping function

#     another_function(func)
#         A function that accepts another function

# FILE
#     functools_wraps_expm.py
#     '''

#     help(a_function)

# '''
# $ functools_wraps_expm.py
# Help on function wrapper in module __main__:

# wrapper()
#     A wrapping function
# '''
