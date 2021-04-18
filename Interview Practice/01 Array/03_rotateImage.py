# You are given an n x n 2D matrix that represents an image. 
# Rotate the image by 90 degrees (clockwise).


import numpy as np
def rotateImage(a):

    return(np.rot90(a, -1))


def rotateImage(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a



def rotateImage(a):
    return list(zip(*reversed(a)))

