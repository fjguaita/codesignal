from itertools import permutations

def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

def stringsRearrangement(a):
    for z in permutations(a):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(a) - 1:
            return True
    return False



a1=["ab", "ad",  "ef",  "eg"]       #true
a2=["abc",  "abx",  "axx",  "abc"]  #true
a3=["ab",   "ad",  "ef",  "eg"]     #false
a4=["aba",  "bbb",  "bab"]          #false

print(stringsRearrangement(a1))
print(stringsRearrangement(a2))
print(stringsRearrangement(a3))
print(stringsRearrangement(a4))

from itertools import permutations
a1=["ab", "ad",  "ef",  "eg"]       #true
for z in permutations(a1):
    a=z
print(a)
for x in zip(a, a[1:]):
    print (*x)



# si puedo reordenar los strings de modo que no haya mas de un caracter distinto entre cada uno es true


