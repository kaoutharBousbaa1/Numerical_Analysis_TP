import math
def f(x):
    x = x**2 -2
def dichotomie(f,a,b,e):
    i = 0
    while(i < e):
        alpha = (a + b) / 2
        if(f(alpha) >= 0):
            b = alpha
        else:
            a = alpha
        i = i + 1
    return alpha
def dichotomie2(f, a, b, e):
    n = int(math.log((b - a)[2]) /(e * math.log((2)[2]))) + 1
    alpha = dichotomie(f, a, b, n)
    return alpha

