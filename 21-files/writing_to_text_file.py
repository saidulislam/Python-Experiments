# The mode='w' parameter means open the file for writing
with open('test.log', mode='w', encoding='utf-8') as a_file:
     a_file.write('test succeeded')
with open('test.log', encoding='utf-8') as a_file:
     print(a_file.read())                              
#test succeeded

# with mode='a' to append to the file instead of overwriting it.
with open('test.log', mode='a', encoding='utf-8') as a_file:
     a_file.write('and again')

with open('test.log', encoding='utf-8') as a_file:
     print(a_file.read())                              
#test succeededand again   
# the encoding parameter that got passed in to the open() 
# function while you were opening a file for writing? It’s important;
# don’t ever leave it out! As you saw in the beginning of this chapter, 
# files don’t contain strings, they contain bytes. Reading a “string” 
# from a text file only works because you told Python what encoding to 
# use to read a stream of bytes and convert it to a string. Writing text 
# to a file presents the same problem in reverse. You can’t write characters 
# to a file; characters are an abstraction. In order to write to the file, 
# Python needs to know how to convert your string into a sequence of bytes. 
# The only way to be sure it’s performing the correct conversion is to 
# specify the encoding parameter when you open the file for writing.    