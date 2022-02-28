import cv2
import numpy as np
from warp import warpTwoImages
from template import nccStitch


# from mi_stitch import miStitch
def stitch(imageA, imageB):
    val = 0
    # ORB function is used
    s = cv2.ORB_create(10000)

    # keypoints and features of imageA and imageB
    # for bigger width and height it does not work
    if (imageA.shape[1] < 32767 and imageB.shape[1] < 32767):
        (kpsA, featuresA) = s.detectAndCompute(imageA, None)
        (kpsB, featuresB) = s.detectAndCompute(imageB, None)
    else:
        H, val, result = nccStitch(imageA, imageB)
        return H, val, result

    # length of keypoints of A and B less than 4  use nccStitch
    if ((len(kpsA) < 4) or (len(kpsB) < 4)):
        H, val, result = nccStitch(imageA, imageB)
        return H, val, result
    print("kps")

    # matcher for two imageA and imageB keyopints
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    matches = bf.knnMatch(featuresA, featuresB, k=2)

    # selecting points from A and B which are nearer to each other
    good = []
    for m, n in matches:
        if m.distance < 0.5 * n.distance:
            good.append([m])

    # getting pointA from imageA and from imageB which satisfy the condition
    pairsOfKp1 = [i[0].queryIdx for i in good]
    pairsOfKp2 = [i[0].trainIdx for i in good]
    pointsA = np.array([kpsA[k].pt for k in pairsOfKp1], np.float32)
    pointsB = np.array([kpsB[t].pt for t in pairsOfKp2], np.float32)

    # length is less than 4 then go to ncc Stitching
    if (len(pointsA) < 4 or len(pointsB) < 4):
        H, val, result = nccStitch(imageA, imageB)
        return H, val, result

    # overlap=maxmin(pointsA,imageA)
    # finding homography
    H, mask = cv2.findHomography(pointsB, pointsA, cv2.RANSAC, 3)
    print(pointsA)
    print(pointsB)
    print(H)

    # H is None the use nccStitch
    if H is None:
        H, val, result = nccStitch(imageA, imageB)
        return H, val, result

    # warp two image A and B
    result = warpTwoImages(imageA, imageB, H)
    return H, val, result