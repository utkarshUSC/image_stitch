import cv2
import numpy as np
from min_max import maxmin
def stitch(imageA,imageB):
        s = cv2.ORB_create(1500)
        (kpsA, featuresA) = s.detectAndCompute(imageA,None)
        (kpsB, featuresB) = s.detectAndCompute(imageB,None)
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(featuresA,featuresB,k=2)


        
        pairsOfKp1 = [i[0].queryIdx for i in matches]
        pairsOfKp2 = [i[0].trainIdx for i in matches]
        pointsA=np.array([kpsA[k].pt for k in pairsOfKp1], np.float32)
        pointsB=np.array([kpsB[t].pt for t in pairsOfKp2], np.float32)
        overlap=maxmin(pointsA,imageB)
        H,mask=cv2.findHomography(pointsA,pointsB,cv2.RANSAC,3)
        imageB=cv2.resize(imageB,(imageB.shape[1],imageA.shape[0]))
        result = cv2.warpPerspective(imageA,H,(int(imageA.shape[1] +(1-overlap)* imageB.shape[1]), imageA.shape[0]))
        
        result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB
       
        return result
