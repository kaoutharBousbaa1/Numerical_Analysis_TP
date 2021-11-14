import numpy as np

def PolyLagrange(X, x, i):
	y = X[i]
	Y = np.concatenate(X[:i], X[i+1:], axis = None)
	res = 1
	for k in range(len(Y)):
		res = res * ((x - Y[k])/(y - Y[K]))
	return res 
