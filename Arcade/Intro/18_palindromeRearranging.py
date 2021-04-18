def palindromeRearranging(s):
    
    return sum([1 for c in s if s.count(c)%2!=0]) <= 1

# da error con los ultimos 2 hidden test
# ni idea por que
# lo cambio por set(s) y se soluciona

def palindromeRearranging(s):   
    return sum([1 for c in set(s) if s.count(c)%2!=0]) <= 1



def palindromeRearranging2(s):

    return sum([s.count(i)%2 for i in set(s)]) <= 1

# hago set(s) para contar una sola vez cada letra
# es mucho mas eficiente que contar 150 veces cuantas letras 'a' hay



def palindromeRearranging3(s):
    s = set()
    for c in s:
        if c in s:
            s.remove(c)
        else:
            s.add(c)
    
    return len(s) <= 1




s1= "aabb"  #true
s2= "abca"  #false
s3= "z"     #true
s4= "aaz"   #true
s5="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbccccaaaaaaaaaaaaa" #false


print(palindromeRearranging(s4))
