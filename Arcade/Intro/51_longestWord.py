import re
def longestWord(text):
    words=re.findall('[A-Za-z]*',text)
    sizes= [len(w) for w in words]
    for w in words:
        if len(w)==max(sizes):
            return w 


def longestWord(text):
    return max(re.split('[^a-zA-Z]', text), key=len)


import string
def longestWord(t):
    return max("".join([i if i in string.ascii_letters else " " for i in t]).split(),key=len)



text= "Ready[[[, steady, go!"
# Expected Output: "steady"