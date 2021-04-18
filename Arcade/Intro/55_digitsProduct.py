import numpy as np
def digitsProduct(product):
    
    for i in range(1, 3600):
        if product == np.prod(list(map(int, str(i)))):
            return i
    
    return -1


print(digitsProduct(26))

