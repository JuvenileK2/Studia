import random

def GraWRulete(): 
    losowanie = random.randint(1, 100)
    while 1:
        losowanie1 = int(input("Odgadnij liczbe: "))
        if(losowanie1 > losowanie): 
            print("Za duzo!")
        elif(losowanie1 < losowanie): 
            print("Za malo!")
        else: 
            print("Brawo, odgadles liczbe")
            break
    return 

Ruleta = GraWRulete() 
print(Ruleta)
