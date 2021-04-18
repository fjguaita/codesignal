def minimumNumberOfBoxes(a, b, f):
    t=max(a,b)
    if t==0: return -1                              #special case when a==b==0
    if a==0 or b==0: return f//t if f%t==0 else -1  #special case when a==0 or b==0

    if b>a:                                         #a little bit change x+y=(f+(b-a)*x)/b
        b,a=a,b                                     #make b<a so that b-a is negative we need 

    t=f//a                                          #to find max value (b-a)*x so that x+y is integer                               
    i=t                                             #start with i=f//a down to 0
    while i>=0:
        k=f+i*(b-a)
        if k%b==0:
            return k/b 
        i-=1 
    return -1


a,b,f = 22,26,70002  # salida 4
print(minimumNumberOfBoxes(a, b, f))