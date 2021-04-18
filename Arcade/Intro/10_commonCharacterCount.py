# cuantos caracteres tienen en común

def commonCharacterCount(s1, s2):
    s1=list(s1)
    s2=list(s2)
    c=0

    for i in s1:
        if i in s2:
            c+=1
            s2.remove(i)

    return c


# siempre una mas copada

def commonCharacterCount2(s1, s2):
    
    return sum([min(s1.count(i),s2.count(i)) for i in set(s1)])


s1= "abca"
s2= "xyzbac"

s3= "zzzz"
s4= "zzzzzzz"

commons1 = set(s1) & set(s2)    # el & me hace una cruza y me deja solo las que se repiten en ambos
commons2 = set(s3) & set(s4)

print(commonCharacterCount(s1,s2))

