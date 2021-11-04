'''
The filter built-in function will take a function and 
an iterable and return an iterator for those elements 
within the iterable for which the passed in function 
returns True. That statement sounds a bit confusing to 
read, so let’s look at an example:
'''

def less_than_ten(x):
    return x < 10

my_list = [1, 2, 3, 10, 11, 12]

# better way to write the following is with lambda function
# for item in filter(lambda x: x < 10, my_list):
for item in filter(less_than_ten, my_list):
    print(item)

#1
#2
#3

