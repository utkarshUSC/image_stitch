import cv2
import numpy as np

def vid2Frame(inputVid, outVidLoc):

    vidcap = cv2.VideoCapture(inputVid)
    success,image = vidcap.read()
    count = 1
    success = True
    while success:
        success,image = vidcap.read()
        print 'Read a new frame: ', success
        cv2.imwrite(str(outVidLoc)+"%d.jpg" % count, image)     # save frame as JPEG file
        count += 1

    return count
