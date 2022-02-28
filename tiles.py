import cv2
import numpy as np

def img2tiles(test_image,windowsize_r,windowsize_c):
        #for converting image into tiles of given windowsizes       
        count=0
      
        # Declare list for adding endpoint for window
        x=[]
        y=[]

        # crop the window and store the endpoints  of window
        for r in range(0,test_image.shape[0]-windowsize_r , windowsize_r):
                for c in range(0,test_image.shape[1] -windowsize_c, windowsize_c):
                        window = test_image[r:r+windowsize_r,c:c+windowsize_c]
                        #checking complete window is of same color and appending the starting coordinate of window
                        if(np.amax(window)!=np.amin(window)) :
                                x.append(r)
                                y.append(c)

                                count+=1

        return count,x,y        


