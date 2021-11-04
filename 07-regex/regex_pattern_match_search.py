import re

text = "The ants go marching one by one"

strings = ['the', 'one']

for string in strings:
    match = re.search(string, text)
    if match:
        print('Found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))


# escape codes
'''
d
: Matches digit

D
: Matches non-digit

s
: Matches whitespace

S
: Matches non-whitespace

w
: Matches alphanumeric

W
: Matches non-alphanumeric

You can use these escape codes inside of a character class, 
like so: [\d]. This would allow us to find any digit and is 
the equivalent of [0-9].
'''