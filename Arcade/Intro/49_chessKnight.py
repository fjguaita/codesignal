def chessKnight(cell):
   
    c = [ord(cell[0])-96,int(cell[1])]
    
    m = [[1,2],[2,1],[1,-2],[-2,1],[-1,2],[2,-1],[-1,-2],[-2,-1]]
    
    return sum([ 1 for i in m  if 0<c[0]+i[0]<9  and  0<c[1]+i[1]<9 ])


cell="a1"

print(chessKnight(cell))
               