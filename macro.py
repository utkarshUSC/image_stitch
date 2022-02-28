import cv2
import numpy as np
from tiles import img2tiles
from score import get_score

image=cv2.imread('3_4.jpg',0)

#window size (number of rows and column)
windowsize_r=64
windowsize_c=64
# Convert Image into tiles
image,count,x,y,score=get_score(image,windowsize_r,windowsize_c)
print("score: ")
print(score)
cv2.imwrite('ok37.bmp',image)