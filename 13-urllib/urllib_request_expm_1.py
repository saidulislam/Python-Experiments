import urllib.request
url = urllib.request.urlopen('https://www.google.com/')
print (url.geturl())
#'https://www.google.com/'

print (url.info())
#<http.client.HTTPMessage object at 0x7fddc2de04e0>

header = url.info()
print (header.as_string())
#('Date: Tue, 17 Jan 2017 11:23:58 GMT\n'
# 'Expires: -1\n'
# 'Cache-Control: private, max-age=0\n'
# 'Content-Type: text/html; charset=ISO-8859-1\n'
# 'P3P: CP="This is not a P3P policy! See '
# 'https://www.google.com/support/accounts/answer/151657?hl=en for more info."\n'
# 'Server: gws\n'
# 'X-XSS-Protection: 1; mode=block\n'
# 'X-Frame-Options: SAMEORIGIN\n'
# 'Set-Cookie: '
# 'NID=80=tYjmy0JY6flsSVj7DPSSZNOuqdvqKfKHDcHsPIGu3xFv41LvH_Jg6LrUsDgkPrtM2hmZ3j9V76pS4K_cBg7pdwueMQfr0DFzw33SwpGex5qzLkXUvUVPfe9g699Qz4cx9ipcbU3HKwrRYA; '
# 'expires=Sat, 24-Dec-2016 18:21:19 GMT; path=/; domain=.google.com; HttpOnly\n'
# 'Alternate-Protocol: 443:quic\n'
# 'Alt-Svc: quic=":443"; ma=2592000; v="34,33,32,31,30,29,28,27,26,25"\n'
# 'Accept-Ranges: none\n'
# 'Vary: Accept-Encoding\n'
# 'Connection: close\n'
# '\n')

print (url.getcode())
#200