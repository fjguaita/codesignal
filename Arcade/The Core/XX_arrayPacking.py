def arrayPacking(a):
    b=[bin(i)[2:] for i in a]
    c="".join(['0'*(8-len(i))+i for i in b[::-1]])
    return int(c,2)


def arrayPacking2(a):
    return sum([a[i] << i*8 for i in range(len(a))])


def arrayPacking3(a):
    return int.from_bytes(a, 'little')


print(arrayPacking([24,85,0]))
print(arrayPacking2([24,85,0]))
print(arrayPacking3([24,85,0]))


a=24
a=bin(a)
a=a[2:]
a='0'*(8-len(a))+a

b=85
b=bin(b)
b=b[2:]
b='0'*(8-len(b))+b
    
c='0b'+(a+b)
c=int(c,2)

a=[24,85,0]
b=[bin(i)[2:] for i in a]
c="".join(['0'*(8-len(i))+i for i in b])

int(c,2)