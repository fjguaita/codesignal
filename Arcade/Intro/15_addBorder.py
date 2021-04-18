# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

def addBorder(picture):
    imagen=[]
    imagen.append("*"*(len(picture[0])+2))
    for line in picture:
        imagen.append("*"+line+"*")
    imagen.append("*"*(len(picture[0])+2))
    return imagen


def addBorder2(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]

def addBorder3(p):
    return ["*"*(len(p[0])+2)]+["*"+i+"*" for i in p]+["*"*(len(p[0])+2)]



picture=["abc",
         "ded"]

picture2=["abcde", 
          "fghij", 
          "klmno", 
          "pqrst", 
          "uvwxy"]


for i in addBorder(picture):
    print (i)

for i in addBorder(picture2):
    print (i)