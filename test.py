import numpy as np
import random

a= np.zeros((3,12)) 

 
 

for i in range(len(a)): 

    for j in range(len(a[i])): 

        if(i == 0): 

            dep = "Santander" 

        elif(i == 1): 

            dep  = "Guajira" 

        else: 

            dep = "Nariño" 

        a[i][j] = (random.randint(18,28))

print(a.max(axis=1))
