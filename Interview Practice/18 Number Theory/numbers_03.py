def modInverse(n, m):
    for i in range (1,m):
        if (n*i)%m==1:
            return(i)
    return(-1)


#print (modInverse(12,13))
#print (modInverse(4,15))


# el mio funciona pero obviamente se pasa de tiempo




def eu(n, m):
    print(n,m)
    if m == 0:
        return n, 1, 0
    else:
        d, x, y = eu(m, n % m)
        return d, y, x - y * (n // m)

def modInverse2(n,m):
    res, x, _ = eu(n, m)
    return x%m if res==1 else -1


print (modInverse2(4,15))



