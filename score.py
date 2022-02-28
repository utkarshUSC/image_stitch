import cv2
import numpy as np
import math
from tiles import img2tiles
from partialDct import p_dct
from coloring import color
from norm import normalize
from tGrad import tenengrad

#calculation of score for tile
def get_score(image,windowsize_r,windowsize_c):
        count,x,y=img2tiles(image,windowsize_r,windowsize_c)
        print("count: "+str(count))

        laplace=np.zeros(count)#declare array for storing laplace gradient foor each tile
        sobel=np.zeros(count)#declare array for storing laplace gradient foor each tile
        score=np.zeros(count)#array for storing score


        for i in range(0,count):
                window=image[x[i]:x[i]+windowsize_r,y[i]:y[i]+windowsize_c]
                sobel[i]=cv2.Sobel(window,cv2.CV_64F,1,0,ksize=5).var()
                laplace[i]=cv2.Laplacian(window,cv2.CV_64F).var()

                #furthrer breakdown of tiles in 8x8 window
                r=8
                c=8
                n,a,b=img2tiles(window,r,c)
                print("n: "+str(n))
                #print(a)
                if(n!=0):

                        score[i]=p_dct(x[i],y[i],a,b,n,image) #calculation of score for tiles
                        print("score["+str(i)+"]: "+str(score[i]))
        
        #normalize all score values of tiles                
        mean=np.mean(score)
        var=np.var(score)
        std_dev=math.sqrt(var)
        score=(score-mean)/std_dev
        


        #make score to lie between 0 to 100
        maximum=np.amax(score)
        minimum=np.amin(score)
        print("maximum: "+str(maximum))
        print("minimum: "+str(minimum))
        score = (score-minimum)*100/(maximum-minimum)
        
              

        #normalizing laplace and sobel value of tiles such that there value lie between 0 and 1                
        laplace=normalize(np.absolute(laplace))       
        sobel=normalize(np.absolute(sobel))
       
        #sobel threshold and laplace threshold
        sobel_th=0.04
        laplace_th=0.04

        #coloring the image with black 
        score,image=color(image,x,y,windowsize_r,windowsize_c,score,count,sobel,sobel_th,laplace,laplace_th)
        return image,count,x,y,score
