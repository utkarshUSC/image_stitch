import cv2
import numpy as np


def color(image,x,y,windowsize_r,windowsize_c,score,count,sobel,sobel_th,laplace,laplace_th):
        old_diff=0
        for i in range(0,count):
                        
                        #finding discontinuity
                        flag=0

                        #initialization of diff value 
                        if(i==0):
                                diff=0 
                        else:   #if difference is positive then diff=1 else diff=0
                                if((score[i]-score[i-1])>0):
                                        diff=1
                                else:
                                        diff=0
                      
                        if(old_diff!=diff   and sobel[i]>sobel_th and laplace[i]>laplace_th):
                                        score[i]=score[i]
                                        flag=1
                                        old_diff=diff
                                                
                                        
                                        a=x[i]+windowsize_r
                                        b=y[i]+windowsize_c
                        
                                        #size lie within image size
                                        if(a < image.shape[0] and b < image.shape[1]):
                                                if(flag==1):
                                                        for k in range(x[i],a,1):
                                                                for l in range(y[i],b,1):
                                                                        image[k,l]=0


                                                
                                                                                                
        return score,image