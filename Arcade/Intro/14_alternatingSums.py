# Several people are standing in a row and need to be divided into two teams. 
# The first person goes into team 1, the second goes into team 2, the third goes into team 1 again, the fourth into team 2, and so on.

# You are given an array of positive integers - the weights of the people. Return an array of two integers, 
# where the first element is the total weight of team 1, and the second element is the total weight of team 2 after the division is complete.



def alternatingSums(a):

    return [sum([a[i] for i in range(len(a)) if i%2==0]),sum([a[i] for i in range(len(a)) if i%2==1])]


# siempre hay uno mas lindo

def alternatingSums2(a):
    return [sum(a[::2]),sum(a[1::2])]


a=[100, 50, 50, 100]



print(alternatingSums(a))