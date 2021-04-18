# Dada una cadena, genera su prefijo más largo que contiene solo dígitos.

def longestDigitsPrefix(s):

    if not s[0].isdigit():
        return ""
    a=[]
    for i in s:
        if i.isdigit():
            a.append(i)
        else:
            break
    return "".join(a)



# sabia que una con findall iba a haber
import re
def longestDigitsPrefix2(s):
    return re.findall('^\d*',s)[0]



s="123aa1"

print(longestDigitsPrefix(s))




import re
s="123aa1"
print(re.findall('^\d*',s))
print(re.findall('\d*',s))
print(re.findall('^\d',s))
print(re.findall('^d*',s))

