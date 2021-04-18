def boxBlur(image):

    r = []
    for i in range(len(image)-2):
        r.append([])
        for j in range(len(image[0])-2):
            r[i].append(sum(image[i][j:j+3] + image[i+1][j:j+3] + image[i+2][j:j+3])//9)
    return r

def boxBlur2(image):
    return [[(sum(sum(x[i:i+3]) for x in image[j:j+3])//9) for i in range(len(image[j])-2)] for j in range(len(image)-2)]


image=[[36,0,18,9,9,45,27], 
       [27,0,54,9,0,63,90], 
       [81,63,72,45,18,27,0], 
       [0,0,9,81,27,18,45], 
       [45,45,27,27,90,81,72], 
       [45,18,9,0,9,18,45], 
       [27,81,36,63,63,72,81]]



print(boxBlur(image))
print(boxBlur2(image))


  