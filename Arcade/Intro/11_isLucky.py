#Ticket numbers usually consist of an even number of digits.
#  A ticket number is considered lucky if the sum of the first half 
# of the digits is equal to the sum of the second half.


def isLucky(n):
    s=str(n)
    half=len(s)//2         
    return sum([int(i) for i in s[:half]])==sum([int(i) for i in s[half:]])



def isLucky2(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))


print(isLucky(123006))