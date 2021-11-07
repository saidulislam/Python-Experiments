a_string = 'PapayaWhip is the new black.'
import io                                          #①
a_file = io.StringIO(a_string)                     #②
print (a_file.read())                              #③
#PapayaWhip is the new black.

print (a_file.read())                              #④
#''
print (a_file.seek(0))                             #⑤
#0

print (a_file.read(10))                            #⑥
#PapayaWhip

print (a_file.tell())                       
#10

print (a_file.seek(18))
#18

print (a_file.read())
#new black.