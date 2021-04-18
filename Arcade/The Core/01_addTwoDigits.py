# You are given a two-digit integer n. Return the sum of its digits.

def addTwoDigits(n):
    return int(str(n)[0]) + int(str(n)[1])


def addTwoDigits2(n):
    return n // 10 + n % 10


print(addTwoDigits(25))


# n // 10   ->   obtengo el primer numero
# n % 10    ->   obtengo el segundo

