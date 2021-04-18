def isAdmissibleOverpayment(p, n, x):

    s=0
    i=-1

    for line in n:
        i+=1
        if line.find('%')!=-1:

            o=float(line[0:line.find('%')])
                        
            if line.find('higher')>0:
                s+=p[i]-p[i]/(1+o/100)
                
            if line.find('lower')>0:
                s+=p[i]-p[i]/(1-o/100)
    
    return (round(s,6)<=x)


prices= [110, 95, 70]
notes= ["10.0% higher than in-store",  "5.0% lower than in-store",  "Same as in-store"]
x= 5

#print (notes)

print(isAdmissibleOverpayment(prices, notes, x))


# esta funcion hace lo mismo

p, n, x = eval(dir()[0])
s = 0
for a, b in zip(p, n):
    f = b < 'S' and eval(b.split('%')[0])/100
    if 'l' in b:
        f = -f
    s+=a/(1+f)*f
return s<=x



        
    