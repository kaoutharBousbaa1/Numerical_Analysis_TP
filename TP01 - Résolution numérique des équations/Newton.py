def f(x)
    x = x**2 - 2
def g(y)
    y = 2*x
def Newton(f, g, alpha, n)
	i = 0
    while(i < n)
        alpha = alpha - f(alpha) / g(alpha)
        i = i + 1
    return alpha
    
    
