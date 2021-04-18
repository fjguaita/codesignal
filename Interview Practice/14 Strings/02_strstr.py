# Avoid using built-in functions to solve this challenge. 
# Implement them yourself, since this is what you would be asked to do during a real interview.

# Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. 
# The function should return an integer indicating the index in s of the first occurrence of x. 
# If there are no occurrences of x in s, return -1.


def strstr(s, x):
    if x not in s:
        return -1
    else:
        for i in range(len(s) - len(x) + 1):
            if  s[i:i+len(x)] == x:
                return i


# con funciones pre-definidas
import re
def findFirstSubstringOccurrence(s, x):
    if re.search(x,s) == None:return -1
    return re.search(x,s).span()[0]



s= "CodefightsIsAwesome"
x= "IsA"