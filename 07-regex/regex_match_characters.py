import re

text = 'abcdfghijk'

# This regular expression pattern means that 
# we are going to look for the letter a, zero or more 
# letters from our class, [b-f] and it needs to end with an f.
parser = re.search('a[b-f]*f', text)
print (parser)
#<_sre.SRE_Match object; span=(0, 5), match='abcdf'>

print (parser.group())
#'abcdf'

# pattern
# xb{1,4}z
# what it says is that we will match things like xbz, xbbz, 
# xbbbz and xbbbbz, but not xz because it doesn’t have a “b”
