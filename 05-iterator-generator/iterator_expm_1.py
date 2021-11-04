my_list = [1, 2, 3]

# print(next(my_list)) # this won't work

list_iterator = iter(my_list)
print (next(list_iterator))
#1

print (next(list_iterator))
#2

print (next(list_iterator))
#3

print (next(list_iterator))
#Traceback (most recent call last):
#  File "/usercode/__ed_file.py", line 16, in <module>
# print (next(list_iterator))
#StopIteration: