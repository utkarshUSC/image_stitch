def maxmin(pointsB,imageB):
        xmin=10000
        
        ct=len(pointsB)
        for k in range(0,ct):
        	if pointsB[k][0] < xmin :
        		xmin = pointsB[k][0]

        		overlap =1- (float(xmin)/imageB.shape[1])

        print("overlap " + str(overlap))
        return overlap
