def firstNotRepeatingCharacter(s):

    if len(s)==1:
        return(s)

    myset=set()   
    
    for i in range(len(s)-1):
        
        if not s[i] in s[(i+1):] and not s[i] in myset:
            return(s[i])
        myset.add(s[i]) 

    return('_')



def firstNotRepeatingCharacter(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'