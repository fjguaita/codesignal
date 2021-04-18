# Find the leftmost digit that occurs in a given string.

def firstDigit(s):
    return [i for i in s if i.isdigit()][0]


print(firstDigit("_Aas_23"))


