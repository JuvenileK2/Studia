def funkcja(a, b):
    i = 0
    while abs(b - a) > 0.05: 
        i += 1
        print(f"wykonanie: {i}")
        print(f"wartosc {round(a, 3)}, {round(b, 3)}") 
        d = 0.62 * (b - a)  
        x1 = a + d  
        x2 = b - d  

        fx1 = (x1**3) + (0.5 * (x1**2)) - (4 * x1) - 1
        fx2 = (x2**3) + (0.5 * (x2**2)) - (4 * x2) - 1

        print(f"Wartosc FX1: {round(fx1, 3)}, FX2: {round(fx2, 3)}") 

        if fx1 > fx2: 
            b = x1 
        elif fx1 < fx2: 
            a = x2 

    print(f"najmniejsza znaleziona wartość z ostatniej iteracji to punkt: {round(b, 5)}, {round(fx2, 5)}")
    return b, fx2

Funkcja = funkcja(-0.5, 5.0) 
print(Funkcja)
