import re
def regexMatching(pattern, test):
    if pattern.count('^')!=0:
        return pattern[1:]==test[:len(pattern)-1]
                
    if pattern.count('$')!=0:
        return pattern[:-1]==test[-(len(pattern)-1):]

    for i in range(0,len(test)-len(pattern)+1):
        if pattern==test[i:i+len(pattern)]:
            return True
    return False
        



def regexMatching(pattern, test):
    p = pattern.strip('[$^]')
    if pattern[0] == '^' and p != test[:len(p)]:
        return False
    if pattern[-1] == '$' and p != test[-len(p):]:
        return False
    return p in test


pattern= "^abcdefghijklmn"
pattern2= "sajdof$"
pattern3= "teywriwlurpewi"
pattern4= "xjcfklsajdof"
test= "abcdefghijklmngskhdgfasteywriwlurpewipoirzxbvvcmnxjcfklsajdof"


print(regexMatching(pattern, test))
print(regexMatching(pattern2, test))
print(regexMatching(pattern3, test))
print(regexMatching(pattern4, test))
