import re

text = "The ants go marching one by one"

strings = ['the', 'one']

for string in strings:

    # Special Note: When you compile patterns, they will get automatically 
    # cached so if you aren’t using lot of regular expressions in your code, 
    # then you may not need to save the compiled object to a variable.
    regex = re.compile(string)
    match = re.search(regex, text)
    if match:
        print('Found "{}" in "{}"'.format(string, text))
        text_pos = match.span()
        print(text[match.start():match.end()])
    else:
        print('Did not find "{}"'.format(string))