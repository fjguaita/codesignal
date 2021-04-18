def evenDigitsOnly(n):
    return sum([1 for i in str(n) if int(i)%2!=0])<1


def evenDigitsOnly(n):
    return all([int(i)%2==0 for i in str(n)])





n= 248622       #true
n2= 642386      #false

print(evenDigitsOnly(n))
