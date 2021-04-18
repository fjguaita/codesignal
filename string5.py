# hasta 150 palabras
# l < 60

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
    # lo que sigue abajo corresponde a la ultima linea

    line = " ".join(line)               # paso de list a un string separando cada palabra con un espacio
    line += (L - len(line)) * " "       # agrego tantos espacios al final como sea necesario
    texto.append(line)                  # agrego esta ultima linea al texto
    return texto



def espaciado(words,l):

    if len(words) == 1:
        return words[0] + (l - len(words[0]))* " "      # tengo que preguntar cuando la linea tiene una sola palabra para no dividir por cero mas abajo
    spaces = l - sum(map(len, words))
    cant_space = (spaces // (len(words) - 1)) * " "
    extra_space = spaces % (len(words) - 1)
    line = ""
    for i,w in enumerate (words[:-1]):                   # voy agregando palabras al renglon excepto la ultima palabra
        line+=w + cant_space + (" " if i < extra_space else "")
    line+=words[-1]
    return line






words=["This",  "is",  "an",  "example",  "of",  "text",  "justification."]

l= 16

# ["This    is    an", 
#  "example  of text", 
#  "justification.  "]


words2=["a", "v", "c", "d", "e"]
l2=3

print(textJustification(words, l))


