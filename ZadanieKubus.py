from math import sin

def golden_ratio(f, a, b, tol):
    PHI = (1 + 5 ** 0.5) / 2
    while abs(b - a) > tol:
        xL, xP = a + (b - a) / PHI**2, b - (b - a) / PHI**2
        if f(xL) < f(xP): 
            b = xP
        else: 
            a = xL
    return (a + b) / 2, f((a + b) / 2)

xmin, fmin = golden_ratio(sin, -3.0, 0.5, 0.05)
print(f"{xmin:.3f}, {fmin:.5f}")
