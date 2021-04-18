import string

def isBeautifulString(s):
    s=[s.count(i) for i in string.ascii_lowercase]
    return sum([1 for a, b in zip(s[:-1], s[1:]) if a<b ]) < 1 



s="bbbaacdafe"
s1="aabbb"
s2="bbc"

print(isBeautifulString(s2))




#s=[s.count(i) for i in sorted(set(string.ascii_lowercase))]
#o=sum([1 for a, b in zip(s[:-1], s[1:]) if a<b ])


