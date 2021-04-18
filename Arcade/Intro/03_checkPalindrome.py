#   el ejercicio 3 devuelve True si la palabra es un palindromo (capicua)

def checkPalindrome(inputString):
    
    for i in range (0,len(inputString)):
        if inputString[i] != inputString[len(inputString)-1-i]:
            return(False)
            
    return(True)



def checkPalindrome2(inputString):
    return inputString == inputString[::-1]     # entiendo que [::-1] da vuelta la palabra



print(checkPalindrome2('neuquen'))
