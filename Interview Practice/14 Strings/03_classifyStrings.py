import re
def classifyStrings(s):
    if re.findall('(([aeiou]{3})|[^aeiou?]{5})',s):
        return 'bad'
    if '?' in s:
        a = classifyStrings(s.replace('?','a',1))
        b = classifyStrings(s.replace('?','n',1))
        return a if a == b else 'mixed'
    return 'good'


s1= "f?ghj"                 #mixed
s2= "?io"                   #mixed
s3= "qwrtl"                 #bad
s4= "aeu"                   #bad
s5= "typ?asdf?relkhfd"      #bad
s6= "?"                     #good
s7="aa?bbb?a?bbb?aa"        #bad



print(classifyStrings(s1))
print(classifyStrings(s2))
print(classifyStrings(s3))
print(classifyStrings(s4))
print(classifyStrings(s5))
print(classifyStrings(s6))
print(classifyStrings(s7))