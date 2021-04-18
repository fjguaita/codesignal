#   el ejercicio 2 consiste en devolver el siglo en función del año

import math
def centuryFromYear(year):
    return(math.ceil(year/100))



def centuryFromYear2(year):
    return (year + 99) // 100


print(centuryFromYear(1810))
