# import urllib.request
# url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
# response = urllib.request.urlopen(url)
# data = response.read()
# with open('test.zip', 'wb') as fobj:
#     fobj.write(data)


# another way to download
# both are valid

# import urllib.request
# url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
# tmp_file, header = urllib.request.urlretrieve(url)
# with open('test.zip', 'wb') as fobj:
#     with open(tmp_file, 'rb') as tmp:
#         fobj.write(tmp.read())


# Specifying Your User Agent

# When you visit a website with your browser, the browser tells the website 
# who it is. This is called the user-agent string. Python’s urllib identifies 
# itself as Python-urllib/x.y where the x and y are major and minor version 
# numbers of Python. Some websites won’t recognize this user-agent string 
# and will behave in strange ways or not work at all. Fortunately, 
# it’s easy for you to set up your own custom user-agent string:

import urllib.request
user_agent = ' Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
url = 'http://www.whatsmyua.com/'
headers = {'User-Agent': user_agent}
request = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(request) as response:
    with open('/home/mdriscoll/Desktop/user_agent.html', 'wb') as out:
        out.write(response.read())