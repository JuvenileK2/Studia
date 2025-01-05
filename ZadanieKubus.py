def funkcja(a, b):
    i = 0
    phi = 0.62  # Stała złotego podziału (zaokrąglona)

    while abs(b - a) > 0.05:  # Warunek zatrzymania
        i += 1
        print(f"wykonanie: {i}\t")
        print(f"wartosc {round(a, 3)}, {round(b, 3)}") 

        # Obliczanie punktów złotego podziału
        d = phi * (b - a)  
        x1 = a + d  
        x2 = b - d  

        # Obliczanie wartości funkcji w punktach x1 i x2
        fx1 = (x1**3) + (0.5 * (x1**2)) - (4 * x1) - 1
        fx2 = (x2**3) + (0.5 * (x2**2)) - (4 * x2) - 1

        print(f"Wartosc FX1: {round(fx1, 3)}, FX2: {round(fx2, 3)}") 

        # Aktualizacja przedziału
        if fx1 > fx2: 
            b = x1  # Zawężamy przedział od prawej strony
        else: 
            a = x2  # Zawężamy przedział od lewej strony

    # Obliczenie minimum
    x_min = (a + b) / 2
    f_min = (x_min**3) + (0.5 * (x_min**2)) - (4 * x_min) - 1

    print(f"najmniejsza znaleziona wartość z ostatniej iteracji to punkt: {round(x_min, 5)}, {round(f_min, 5)}")
    return x_min

# Wywołanie funkcji
Funkcja = funkcja(-0.5, 5.0)
print(Funkcja)
