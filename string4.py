def classifyStrings(s):

    if len(s)<=2:
        return 'good'

    if '?' not in s:
        for i in range(len(s)-2):
            if vocal(s[i:i+3])==3:
                return 'bad'
        for i in range(len(s)-4):
            if vocal(s[i:i+5])==0:
                return 'bad'
        return 'good'
    else:
        for i in range(len(s)-2):
            if vocal(s[i:i+3])==3:
                return 'bad'
        for i in range(len(s)-4):
            if vocal(s[i:i+5])==0 and '?' not in s[i:i+5]:
                return 'bad'
        return 'mixed'

def vocal(s):
    vocales=['a','e','i','o','u']
    return sum([1 for i in s if i in vocales])

# funcionaba casi perfecto, dio error con un par de los ultimos
# "aa?bbb?a?bbb?aa" o "aa?bbbb" que deberian ser bad y sale mixed



import re
def classifyStrings2(s):
    if re.findall('(([aeiou]{3})|[^aeiou?]{5})',s):
        return 'bad'
    if '?' in s:
        a = classifyStrings2(s.replace('?','a',1))
        b = classifyStrings2(s.replace('?','n',1))
        return a if a == b else 'mixed'
    return 'good'


s1= "f?ghj"                 #mixed
s2= "?io"                   #mixed
s3= "qwrtl"                 #good
s4= "aeu"                   #bad
s5= "typ?asdf?relkhfd"      #bad
s6= "?"                     #good



classifyStrings2("aa?bbb?a?bbb?aa")
