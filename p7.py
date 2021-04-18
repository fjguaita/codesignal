import numpy as np

def isCryptSolution(c, s):
    s=np.array(s)
    l=s[0:,0]
    v=s[0:,1]
    r=[]
    for i in c:
        x=str()
        for j in i:
            x+=(f'{int(v[np.where(l==j)])}')
            if len(x)>1 and x[0]=='0':
                return False
        r.append(int(x))

    return (r[0]+r[1]==r[2])


def isCryptSolution2(crypt, solution):
    dic = {ord(c): d for c, d in solution}
    *v, = map(lambda x: x.translate(dic), crypt)
    return not any(x != "0" and x.startswith("0") for x in v) and int(v[0]) + int(v[1]) == int(v[2])




c=["SEND",  "MORE",  "MONEY"]

s=[["O","0"], 
  ["M","1"], 
  ["Y","2"], 
  ["E","5"], 
  ["N","6"], 
  ["D","7"], 
  ["R","8"], 
  ["S","9"]]


c2= ["TEN",   "TWO",  "ONE"]
s2=[["O","1"], 
   ["T","0"], 
   ["W","9"], 
   ["E","5"], 
   ["N","4"]]


# aprender a usar diccionarios y punteros a mapas
d=dict(s2)
dic = {ord(h): k for h, k in s2}    #la funcion ord devuelve el codigo ASCII o Unicode de la letra
*v = map(lambda x: x.translate(dic), c2)    #translate reemplaza caracteres según una tabla dada
print(dic)
print(v)

print(isCryptSolution(c,s))

