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



def isCryptSolution(crypt, solution):
    dic = {ord(c): d for c, d in solution}
    *v, = map(lambda x: x.translate(dic), crypt)
    return not any(x != "0" and x.startswith("0") for x in v) and \
        int(v[0]) + int(v[1]) == int(v[2])



def isCryptSolution(crypt, solution):
    table = str.maketrans(dict(solution))
    t = tuple(s.translate(table) for s in crypt)
    zeroes = any(s[0] == '0' for s in t if len(s) > 1)
    return not zeroes and int(t[0]) + int(t[1]) == int(t[2])


crypt=["SEND",  "MORE",  "MONEY"]
solution=[["O","0"], 
          ["M","1"], 
          ["Y","2"], 
          ["E","5"], 
          ["N","6"], 
          ["D","7"], 
          ["R","8"], 
          ["S","9"]]