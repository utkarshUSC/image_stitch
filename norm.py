import numpy as np
import math

#function for normalizing the value between 0 and 1
def normalize(t):
	
	#standardize the value
	mean=np.mean(t)
	var=np.var(t)
	std_dev=math.sqrt(var)
	t=(t-mean)/std_dev

	#making value lie between 0 and 1
	maximum=max(t)
	minimum=min(t)
	t=(t-minimum)/(maximum-minimum)
	
	#print and return t
	print("t: ")
	print(t)
	return t