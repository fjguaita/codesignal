def firstDuplicate(a):
    mySet=set()
    for i in a:
        if i in mySet:
            return i
        mySet.add(i)
    return -1


