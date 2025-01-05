def ZlotyPodzial(a, b, tol=0.05):  
    k = 0.62 
    d = k * (b - a)  
    xL = b - d
    xP = a + d
    fx1 = (xL**3) + (0.5 * (xL**2)) - (4 * xL) - 1
    fx2 = (xP**3) + (0.5 * (xP**2)) - (4 * xP) - 1
    i = 0  
    while abs(b - a) > tol: 
        i += 1
        print(f"Iteracja nr: {i}")
        
        if fx1 < fx2: 
            b, xP, fx2 = xP, xL, fx1
            d = k * (b - a)  
            xL = b - d
            fx1 = (xL**3) + (0.5 * (xL**2)) - (4 * xL) - 1
        else: 
            a, xL, fx1 = xL, xP, fx2
            d = k * (b - a)  
            xP = a + d
            fx2 = (xP**3) + (0.5 * (xP**2)) - (4 * xP) - 1

        print(f"Wartosc xL wynosi: {xL}, a wartosc xP wynosi: {xP}")
    
    xmin = (a + b) / 2
    f_min = (xmin**3) + (0.5 * (xmin**2)) - (4 * xmin) - 1
    
    return xmin, f_min

Funkcja = ZlotyPodzial(-0.5, 5.0, tol=0.05)
print(Funkcja)
