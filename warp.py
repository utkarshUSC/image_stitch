import cv2
import numpy as np
import math
from itertools import product
import sys
#res_max for storing highest correlation value, x for storing corresponding x coordimate, interval
def warpTwoImages(img1, img2, H):
    '''warp img2 to img1 with homograph H'''
    h1,w1 = img1.shape[:2]
    h2,w2 = img2.shape[:2]

    pts1 = np.float32([[0,0],[0,h1],[w1,h1],[w1,0]]).reshape(-1,1,2)
    pts2 = np.float32([[0,0],[0,h2],[w2,h2],[w2,0]]).reshape(-1,1,2)

    #points after translation on image
    pts2_ = cv2.perspectiveTransform(pts2, H)
    pts = np.concatenate((pts1, pts2_), axis=0)

    #getting maximum and minimum x and y coordinates
    [xmin, ymin] = np.int32(pts.min(axis=0).ravel() - 0.5)
    [xmax, ymax] = np.int32(pts.max(axis=0).ravel() + 0.5)


    t = [-xmin,-ymin]
    Ht = np.array([[1,0,t[0]],[0,1,t[1]],[0,0,1]]) # translation matrix
    H1=np.dot(Ht,H)#getting modified homography matrix

    print(img2.shape)
    result=cv2.warpPerspective(img2,H1,(xmax-xmin,ymax-ymin))
    result[t[1]:h1+t[1],t[0]:w1+t[0]] = img1
    return result