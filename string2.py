
import re
s="ah, hola zanahoria como andas, como haces para cagar como un mono holandes"
s2= "vSKwWDjwIerQKMgVaAeaniorRJlpaierb"

print(re.findall("como",s)) 
print(re.findall('\\bh\w+\\b',s))           # devuelve todas las palabras que empiecen con h        \\b es para buscar las palabras separadas por espacios
print(re.findall('h\w+',s))                 # devuelve todas las palabras que tienen h, de la h hasta el final
print(re.findall('[A-Z]',s2))               # devuelve las mayusculas
print(re.findall('[a-z]',s2))               # devuelve las minusculas
print(re.findall(r'[A-Za-z][a-z]*',s2))     # devuelve las mayusculas seguidas de minusculas
print(re.findall('[A-Za-z][a-z]*',s2))       # devuelve la primer mayuscula o minuscula seguida de una minuscula que encuentra y sigue

# no se que hace la r
# el * entiendo es para multiplicar y que siga agregando las minusculas

print(re.findall('([aeiou]{3})',s2.lower()))    #busca 3 vocales juntas, si hay mas, muestra las primeras 3
print(re.findall('([^aeiou?]{5})',s2.lower()))  #busca 5 caracteres juntos que no sean vocales ni ?
print(re.findall('[A-Z][a-z]*',s2))
print(re.findall('[A-Z][a-z]',s2))

