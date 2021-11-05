# importing the required module
import timeit
 
# code snippet to be executed only once
mysetup = "from math import sqrt"
 
# code snippet whose execution time is to be measured
mycode = '''
def example():
    mylist = []
    for x in range(100):
        mylist.append(sqrt(x))
'''
 
# timeit statement
print (timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 10000))

# The output of above program will be the execution 
# time(in seconds) for 10000 iterations of the code 
# snippet passed to timeit.timeit() function.