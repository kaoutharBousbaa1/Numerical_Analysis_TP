import math
def f(x):
    x = x**2 -2
def g(y):
    y = 2*x
def dichotomie(f,a,b,n):
    i = 0
    while(i < n):
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
def Newton(f, g, alpha, n):
    i = 0
    while(i < n):
        alpha = alpha - f(alpha) / g(alpha)
        i = i + 1
    return alpha
a, b, x, n = 1, 3, 2, 3
print("-----------------Pour 3 itérations-----------------\n")
print("La valeur approchée de la racine de 2 par la méthode de dichotomie est :\n", dichotomie(f, a, b, n))
print("La valeur approchée de la racine de 2 par la méthode de Newton est :\n\n", Newton(f, g, x, n))
n = 10
print("-----------------Pour 10 itérations-----------------\n")
print("La valeur approchée de la racine de 2 par la méthode de dichotomie est :\n", dichotomie(f, a, b, n))
print("La valeur approchée de la racine de 2 par la méthode de Newton est :\n\n", Newton(f, g, x, n))
n = 30
print("-----------------Pour 30 itérations-----------------\n")
print("La valeur approchée de la racine de 2 par la méthode de dichotomie est :\n", dichotomie(f, a, b, n))
print("La valeur approchée de la racine de 2 par la méthode de Newton est :\n\n", Newton(f, g, x, n))
