import numpy as np

def PolyLagrange(X, x, i):
	y = X[i]
	Y = np.concatenate(X[:i], X[i+1:], axis = None)
	res = 1
	for k in range(len(Y)):
		res = res * ((x - Y[k])/(y - Y[K]))
	return res 

def InterLagrange(X, f, x):
	L = []
	for i in range(len(X)):
		L += f(X[i])*PolyLagrange(X, x, i)
	res = sum(L)
	return res
	
