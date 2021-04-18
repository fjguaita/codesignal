def amendTheSentence(s):
    s = list(s)
    for i,x in enumerate(s):
        print(i)
        if x.isupper():
            s[i] = x.lower()
            if i != 0:
                s[i] = ' ' + s[i]
    return ''.join(s)


import re
def amendTheSentence(s):
    return " ".join(re.findall(r"[A-Za-z][a-z]*", s)).lower()