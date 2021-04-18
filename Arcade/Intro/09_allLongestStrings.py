
def allLongestStrings(s):
    
    a=[len(i) for i in s]    
    return [j for i, j in zip(a,s) if i==max(a) ]


# un poquito mas simple

def allLongestStrings2(inputArray):
    m = max(len(s) for s in inputArray)
    return [s for s in inputArray if len(s) == m]




s1=["aba",  "aa",  "ad",  "vcd",  "aba"]


s2=["young",  "yooooooung",  "hot",  "or",  "not",  "come",  "on",  "fire",  "water",  "watermelon"]



print(allLongestStrings2(s2))

