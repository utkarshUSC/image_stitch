import cv2
import numpy as np
from v2f import vid2Frame
from image_stitch import stitch
'''
inputVid="ImageStitching.wmv"
outVidLoc="IM"
count=vid2Frame(inputVid,outVidLoc)
'''
outVidLoc="IM"
count=246
interval = 40
imageA=cv2.imread(str(outVidLoc)+ str(1)+".jpg",0)
for j in range(2,count, interval):
         imageB=cv2.imread(str(outVidLoc)+ str(j)+".jpg",0)
         result=stitch(imageA,imageB)
         imageA=result
cv2.imwrite('all_combine2.jpg', result)
        
	