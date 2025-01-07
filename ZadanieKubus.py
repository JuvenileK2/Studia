import math as sin 

def f(x):
    return x**3 + 0.5 * x**2 - 4 * x - 1 

def golden_section_search_table(f, a, b, tol):
    phi = (1 + 5 ** 0.5) / 2
    resphi = 2 - phi

    xL = a + resphi * (b - a)
    xP = b - resphi * (b - a)
    f_xL = f(xL)
    f_xP = f(xP)

    while abs(b - a) > tol:
        if f_xL < f_xP:
            b, xP, f_xP = xP, xL, f_xL
            xL = a + resphi * (b - a)
            f_xL = f(xL)
        else:
            a, xL, f_xL = xL, xP, f_xP
            xP = b - resphi * (b - a)
            f_xP = f(xP)

    x_min = (a + b) / 2
    f_min = f(x_min)

    return x_min, f_min

tolerance = 0.05
x_min, f_min = golden_section_search_table(f, 0.5, 5.0, tolerance)
print(f"{x_min:.3f}, {f_min:.5f}")