def deleteDigit(n):
    a=[]
    z=list(str(n))
    for i in range(len(z)):
        z.pop(i)
        a.append(int("".join(z)))
        z=list(str(n))
    return max(a)



def deleteDigit(n):
    n = str(n)
    return max(int(''.join(n[:i]+n[i+1:])) for i in range(len(n)))


def deleteDigit(n):
    return max([int(str(n)[:i] + str(n)[i+1:]) for i in range(len(str(n)))])