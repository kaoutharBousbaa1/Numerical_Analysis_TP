from matplotlib.pylab import plot, show
def f(x)
    x = x**3 - x - 3
def g(y)
    y = 3**2 - 1
def Newton(f, g, alpha, n)
    l = [0]
    while(n <= 100)
        alpha = alpha - f(alpha) / g(alpha)
        n = n + 1
	l = l + [alpha]
    plot(l)
    show()
    grid()
    return alpha

n = 0
print("------------------------Pour alpha_zero = 0----------------------------\n")
alpha = Newton(f, g, 0, n)
print("------------------------Pour alpha_zero = 1----------------------------\n")
alpha = Newton(f, g, 1, n)

