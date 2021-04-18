#%%
import numpy as np
import time

start_time=time.time()
def sudoku2(grid):

    grid=np.array(grid)
    
    for i in range(9):
        aux=np.delete(grid[i,:],np.where(grid[i,:]=='.'))
        if aux.size!=np.unique(aux).size:
            return False
        aux=np.delete(grid[:,i],np.where(grid[:,i]=='.'))
        if aux.size!=np.unique(aux).size:
            return False
    
    for i in range(3):
        for j in range(3):
            aux=grid[3*i:3*i+3,3*j:3*j+3].reshape(9)
            aux=np.delete(aux,np.where(aux=='.'))
            if aux.size!=np.unique(aux).size:
                return False        
    return True   
    
    

  

grid=  [[".",".",".",".",".",".","5",".","."], 
        [".",".",".",".",".",".",".",".","."], 
        [".",".",".",".",".",".",".",".","."], 
        ["9","3",".",".","2",".","4",".","."], 
        [".",".","7",".",".",".","3",".","."], 
        [".",".",".",".",".",".",".",".","."], 
        [".",".",".","3","4",".",".",".","."], 
        [".",".",".",".",".","3",".",".","."], 
        [".",".",".",".",".","5","2",".","."]]


print(sudoku2(grid))
print(time.time()-start_time)


#%%

import time

start_time=time.time()

def check_unique(nums):
    s = set()
    for num in nums:
        if num == '.':
            continue 
            
        if num in s:
            return False
        s.add(num)
    return True
        

def sudoku2(grid):
    for line in grid:
        if not check_unique(line):
            return False
    
    for i in range(9):
        if not check_unique([line[i] for line in grid]):
            return False
        
    for i in range(0,9,3):
        for j in range(0, 9, 3):
            if not check_unique(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
                return False
            
    return True



grid=  [[".",".",".",".",".",".","5",".","."], 
        [".",".",".",".",".",".",".",".","."], 
        [".",".",".",".",".",".",".",".","."], 
        ["9","3",".",".","2",".","4",".","."], 
        [".",".","7",".",".",".","3",".","."], 
        [".",".",".",".",".",".",".",".","."], 
        [".",".",".","3","4",".",".",".","."], 
        [".",".",".",".",".","3",".",".","."], 
        [".",".",".",".",".","5","2",".","."]]


print(sudoku2(grid))
print(time.time()-start_time)


# %%


grid=[[1,3,2,5,4,6,9,8,7], 
      [4,6,5,8,7,9,3,2,1], 
      [7,9,8,2,1,3,6,5,4], 
      [9,2,1,4,3,5,8,7,6], 
      [3,5,4,7,6,8,2,1,9], 
      [6,8,7,1,9,2,5,4,3], 
      [5,7,6,9,8,1,4,3,2], 
      [2,4,3,6,5,7,1,9,8], 
      [8,1,9,3,2,4,7,6,5]]

import numpy as np

grid=np.array(grid)


i=0
j=0
aux=(grid[i:i+3,j:j+3].reshape(1,9)).tolist() 
aux2=grid[:,i].tolist()
set(*aux)


aux=aux.reshape(1,9)