import cv2
import sys
import numpy as np
import math
from warp import warpTwoImages


# res_max for storing highest correlation value, x for storing corresponding x coordimate, interval

def nccStitch(imageA, imageB):
    # for normalized crossed correlation
    res_max = -1
    xA1 = -1
    yA1 = -1

    method = 'cv2.TM_CCORR_NORMED'
    # window size for ncc calculation
    intervalx = 256
    intervaly = 256

    # moving window by 64x64 and taking consideration only 40 percentage of imageB which is shorter in width
    for i in range(imageA.shape[1] - int(imageB.shape[1] * 0.4), imageA.shape[1], 64):
        for j in range(0, imageA.shape[0], 64):
            template = imageA[j:j + intervaly, i:i + intervalx]  # template
            sobelx = cv2.Sobel(template, cv2.CV_32F, 1, 0, ksize=15)
            sobely = cv2.Sobel(template, cv2.CV_32F, 0, 1, ksize=15)
            template = sobelx + sobely  # to get gradient of image

            temp = imageB[0:imageB.shape[0], 0:int(imageA.shape[1] * 0.4)]  # temp
            sobelx = cv2.Sobel(temp, cv2.CV_32F, 1, 0, ksize=15)
            sobely = cv2.Sobel(temp, cv2.CV_32F, 0, 1, ksize=15)
            temp = sobelx + sobely  # to get gradient of image in both direction

            # for reducing the white background for template
            temp = cv2.subtract(temp, cv2.mean(template))
            template = cv2.subtract(template, cv2.mean(template))

            # applying matching of template in temp
            res = cv2.matchTemplate(temp, template, 3)
            _, val, _, loc = cv2.minMaxLoc(
                res)  # val stores highest correlation from temp, loc stores coresponding starting location in temp
            if (val > res_max):
                res_max = val
                xA1 = i
                yA1 = j
                xB1 = loc[0]
                yB1 = loc[1]
                print(val)

    # getting overlap between two images
    overlap = (1 - float(xA1) / imageA.shape[1])
    print("overlap: " + str(overlap))

    # change=int(imageA.shape[0]*0.2)
    pointsA = [[xA1, yA1], [xA1 + intervalx, yA1], [xA1, yA1 + intervaly], [xA1 + intervalx, yA1 + intervaly]]
    pointsB = [[xB1, yB1], [xB1 + intervalx, yB1], [xB1, yB1 + intervaly], [xB1 + intervalx, yB1 + intervaly]]

    print(xA1)
    print(xB1)
    # finding homography
    H, mask = cv2.findHomography(np.asarray(pointsB, float), np.asarray(pointsA, float), cv2.RANSAC, 3)

    # warping two images
    result = warpTwoImages(imageA, imageB, H)
    return H, res_max, result