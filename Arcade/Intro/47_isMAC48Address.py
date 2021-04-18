import re
def isMAC48Address(s):
    if len(s)!=17:
        return False 
    for i in s.split('-'):
        if "".join(re.findall('[0-9A-F]',i))!=i:
            return False
    return True if len(s.split('-'))==6 else False
    
    
    
def isMAC48Address(s):
    return bool(re.match(('^' + '[\dA-F]{2}-' * 6)[:-1] + '$', s))
    
    
def isMAC48Address(inputString):
    return re.match("^([0-9A-F]{2}-){5}[0-9A-F]{2}$", inputString) is not None
    
    
def isMAC48Address(inputString):

    return bool(re.match('^([0-9A-F]{2}-){5}([\dA-F]{2})$', inputString))


s="00-1B-63-84-45-E6"
s1="Z1-1B-63-84-45-E6"
s2="not a MAC-48 address"


