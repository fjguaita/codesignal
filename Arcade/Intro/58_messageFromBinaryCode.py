def messageFromBinaryCode(code):
    string_blocks = (code[i:i+8] for i in range(0, len(code), 8)) 
    return ''.join(chr(int(char, 2)) for char in string_blocks)




 =  sum([bin(i).count('1') for i in range(a,b)])




bin(85)
bin(85)[2:]
bin(85)[::-1]
bin(85)[2:][::-1]