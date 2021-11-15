import numpy as np
import matplotlib.pyplot as plt

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
def courbe(f, a, b, n, p):
	X = np.linspace(a, b, n+1)
	Y = f(X)
	pts_traces = np.linspace(a, b, (n+1)*p)
	Y_courbe_f = f(pts_traces)
	Y_courbe_p = []
	for x in pts_traces:
		Y_courbe_P += InterLagrange(X, f, x)
	plt.plot(X, Y)
	plt.plot(pts_traces, Y_courbe_f)
	plt.plot(pts_traces, Y_courbe_p)
	plt.grid()
	plt.show()
print("Courbe de la fonction f, de la fonction polynomiale P, ainsi que les points d'interpolations: \n")
print("-------------------f = sin; a = 0; b = 2*pi; n = 3------------------\n")
f = lambda x : np.sin(x)
a = 0
b = 2 * np.pi
n = 3
p = 5
courbe(f, a, b, n, p)
print("-------------------f = sin; a = 0; b = 2*pi; n = 10------------------\n")
n = 10
courbe(f, a, b, n, p)
print("-------------------f = sin; a = 0; b = 2*pi; n = 20------------------\n")
n = 20
courbe(f, a, b, n, p)
print("-------------------f = exp; a = -10; b = 10; n = 3------------------\n")
f = lambda x : np.exp(x)
a = -10
b = 10
p = 5
n = 3
courbe(f, a, b, n, p)
print("-------------------f = exp; a = -10; b = 10; n = 10------------------\n")
n = 10
courbe(f, a, b, n, p)
print("-------------------f = exp; a = -10; b = 10; n = 20------------------\n")
n = 20
courbe(f, a, b, n, p)











