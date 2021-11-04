import re

# finding the first match
silly_string = "the cat in the hat"
pattern = "the"
match = re.search(pattern, silly_string)
print (match.group())
#'the'

# finding multiple matches
silly_string = "the cat in the hat"
pattern = "the"
print (re.findall(pattern, silly_string))
#['the', 'the']


# using finditer
silly_string = "the cat in the hat"
pattern = "the"

for match in re.finditer(pattern, silly_string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=match.group(), begin=match.start(),
        end=match.end())
    print(s)