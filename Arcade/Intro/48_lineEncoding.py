import re
def lineEncoding(s):
    counted = re.findall(r'((\w)\2*)', s)
    return "".join([ str(len(c[0])) + c[1] if len(c[0]) > 1 else str(c[0]) for c in counted])

s = "aabbbc"    

print(lineEncoding(s))

import re
s = "aabbbc" 
counted=(re.findall(r'((\w)\2*)', s))
for i in counted:
    print (i)