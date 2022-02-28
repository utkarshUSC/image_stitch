import cv2
import math
import numpy as np
from v2f import vid2Frame
from image_stitch import stitch
from warp import warpTwoImages
from border_up import border

# start name of image
outVidLoc = "Clips/3_4/image_"
count = 10
imageA = cv2.imread(str(outVidLoc) + str(235) + ".jpg", 0)  # from left to right
# imageA=cv2.imread("brisk2.jpg",0)

val = 0
for j in range(1, count):
    imageB = cv2.imread(str(outVidLoc) + str(235 + j) + ".jpg", 0)
    # imageA=cv2.imread("image_499.jpg",0)
    print(j)
    H, val, result = stitch(imageA, imageB)
    imageA = result
    cv2.imwrite("brisk" + str(j) + ".jpg", result)

cv2.imwrite('brisk.jpg', result)