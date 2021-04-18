def electionsWinners2(v, k):
    c, mv = 0, max(v)
    if k==0 and v.count(mv)==1: c=1
    for i in v: 
        if i+k>mv: c+=1
    return c


def electionsWinners3(v, k):
    m = max(v)
    
    return int(v.count(m) == 1) if k == 0 else len([n for n in v if m < n + k])


    

votes= [2, 3, 5, 2]
k= 3

