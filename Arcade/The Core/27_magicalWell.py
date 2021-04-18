def magicalWell(a, b, n):
    o=0
    while n>0:
        o+=a*b
        a+=1
        b+=1
        n-=1
    return o




def magicalWell2(a, b, n):
    return sum([(a + i) * (b + i) for i in range(n)])


print(magicalWell(1, 2, 2))             # 8
print(magicalWell(1936, 1835, 5))       # 17800540





