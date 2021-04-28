def chessBoardCellColor(c1, c2):

    return sum([ord(c1[0])+int(c1[1])])%2==sum([ord(c2[0])+int(c2[1])])%2





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
   