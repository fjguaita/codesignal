a=['(',')']
b=['[',']']
c=['{','}']
    
condicion=True

sequence='(afdsjlkafd)'
    
while condicion:
    print(sequence)
    if sequence[0]==a[0] and sequence[len(sequence)-1]==a[1]:
        aux=len(sequence)-2
        sequence=sequence[1:len(sequence)-2]
    else:
        condicion=False


    
    while condicion:
        condicion=False
        if sequence[0]==a[0] and sequence[len(sequence)-1]==a[1] or sequence[0]==b[0] and sequence[len(sequence)-1]==b[1] or sequence[0]==c[0] and sequence[len(sequence)-1]==c[1]:
            sequence=sequence[1:len(sequence)-2]

sequence='[]'
sequence=sequence[1:len(sequence)-2]
if len(sequence)==0:
    print(1)

sequence='[]'
if sequence.count('[') == sequence.count(']'):
    print('1')

