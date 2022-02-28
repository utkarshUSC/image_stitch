import cv2
import numpy as np
from norm import normalize

def p_dct(x,y,a,b,n,image):
        score=0.0 #initializing score

        u=np.float32(np.zeros(n)) 
        w=0.0 #variable for storing weight
        
        for j in range(0,n):
            z=0
            column=x+a[j]
            row=y+b[j]
            window=image[column:column+8,row:row+8] #window for partial dct
            imf=np.float32(window)
            temp=cv2.dct(imf) #calculation of partial dct
            #print(temp)
            
            for m in range(0,temp.shape[0]):
                for p in range(0,temp.shape[1]):
                    u[j]=u[j]+temp[m,p] #taking sum of all the value from dctcoefficient  

            
            #providing weightage to higher dct coefficient value by multiplying them with their own value
            score=score+u[j]*u[j]

            w=w+u[j] #sum of all weightage
        
      
        #divide the value with their weightage sum
        return score/w