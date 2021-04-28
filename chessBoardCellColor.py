def chessBoardCellColor(c1, c2):

    return sum([ord(c1[0])+int(c1[1])])%2==sum([ord(c2[0])+int(c2[1])])%2



def chessBoardCellColor2(cell1, cell2):
    
    return (ord(cell1[0])+int(cell1[1])+ord(cell2[0])+int(cell2[1]))%2==0



def chessBoardCellColor3(cell1, cell2):
    return (sum(map(ord,cell1+cell2)))%2 == 0


cell1= "A1"
cell2= "C3"

# determinar si las casillas tienen el mismo color
# tablero ajedrez

#   A8 B8 C8 D8 E8 F8 G8 I8
#   A7 B7
#   A6
#   A5
#   A4
#   A3
#   A2
#   A1

print(chessBoardCellColor(cell1, cell2))