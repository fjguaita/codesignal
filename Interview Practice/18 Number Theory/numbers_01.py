# You are supposed to label a bunch of boxes with numbers from 0 to n, and all the labels are stored in the array arr. 
# Unfortunately one of the labels is missing. Your task is to find it.

def missingNumber(arr):
    
    for i in range(len(arr)):
        if not i in arr:
            return i
    return len(arr)



def missingNumber2(arr):
    l = len(arr)
    s = (l*(l+1))/2
    return s - sum(arr)




arr= [3, 1, 0]

print(missingNumber(arr))
print(missingNumber2(arr))