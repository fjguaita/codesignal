import math

def simplifyRational2(n, d):
    t=math.gcd(n,d)
    m,n=n/t,d/t 
    if n<0:
        return [-m,-n]
    return [m,n]


# math.gcd find the greatest common divisor of the two integers

n= -88
d= 24


print(simplifyRational2(n,d))        












