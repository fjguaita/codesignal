def textJustification(words, L):
        
    texto = []
    line = []
    l = 0
    for word in words:
        if l + len(word) > L:
            texto.append(espaciado(line, L))
            l = 0
            line = []
        line.append(word)
        l += 1 + len(word)
    line = " ".join(line)              
    line += (L - len(line)) * " "      
    texto.append(line)                  
    return texto



def espaciado(words,l):
    if len(words) == 1:
        return words[0] + (l - len(words[0]))* " "
    spaces = l - sum(map(len, words))
    cant_space = (spaces // (len(words) - 1)) * " "
    extra_space = spaces % (len(words) - 1)
    line = ""
    for i,w in enumerate (words[:-1]):     
        line+=w + cant_space + (" " if i < extra_space else "")
    line+=words[-1]
    return line

words=["Looks", "like", "it", "can", "be", "a", "tricky", "test"]
l= 25

print(textJustification(words, l))




