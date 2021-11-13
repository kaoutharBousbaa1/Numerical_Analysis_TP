from matplotlib.pylab import plot, show
import numpy as np
def f(x):
    x = x**3 - x - 3
def g(y):
    y = 3**2 - 1
def Newton(f, g, alpha, n):
    l = [0]
    while(n <= 100):
        alpha = alpha - f(alpha) / g(alpha)
        n = n + 1
	l = l + [alpha]
    plot(l)
    show()
    return alpha
x = np.linspace(-3, 3, 100)
y = f(x)
plot(x, y)
grid()
show()

