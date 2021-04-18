import re
def sumUpNumbers(s):
    return sum([int(i) for i in re.findall('\d*',s) if i.isdigit()])


def sumUpNumbers(s):
    return sum(map(int,"".join([i if i.isdigit() else " " for i in s]).split()))

s="2 apples, 12 oranges"

print(sumUpNumbers(s))



product=26

