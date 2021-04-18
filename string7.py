def isLucky(n):
    s=list(str(n))
             
    return sum([int(i) for i in s[:len(s)//2]])==sum([int(i) for i in s[len(s)//2:]])



# lo mismo pero mas limpio

def isLucky2(n):
    s = [int(x) for x in str(n)]
    l = int(len(s)/2)    
    return sum(s[:l]) == sum(s[l:])


print(isLucky(1524))

n=1520
s = [int(x) for x in str(n)]

