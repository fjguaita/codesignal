# Given an integer n, return the largest number that contains exactly n digits.


def largestNumber(n):
    o=[]
    for i in range(n):
        o.append('9')
    return int("".join(o))



def largestNumber2(n):
    return 10 ** n - 1


def largestNumber3(n):
    return int('9' * n)




print(largestNumber(4))


