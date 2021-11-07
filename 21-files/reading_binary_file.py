an_image = open('cat.jpg', mode='rb')
print (an_image.mode)
#rb

print (an_image.name)
#'cat.jpg'

# print (an_image.encoding)

an_image = open('cat.jpg', mode='rb') 
print (an_image.tell())
#0

data = an_image.read(3)          #①
print (data)
#b'\xff\xd8\xff'

print (type(data) )              #②
#<class 'bytes'>

print (an_image.tell())          #③
#3

print (an_image.seek(0))
#0

data = an_image.read()
print (len(data))
#4749