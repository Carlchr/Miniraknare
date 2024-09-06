#Funktionen använder talhantering från mainmetoden
def ratt_raknesatt(Talhantering):
    #När talhantering är en av re räknesätten så ges möjligheten att skriva tal 1, men annars så skrivs ett felmmeddelande och 
    while True: 
        if Talhantering in ["+", "-", "*", "/"]:
            Tal1_int = int(input("Tal 1: "))
            return Tal1_int
        else:
            print("error, försök igen")
            Talhantering = input("Hur vill du hantera talen? ")
            break


#Funktionen använder talhantering och tal1_int från mainmetoden
def calculations(Talhantering, Tal1_int):

    #har det här istället för main för att då behöver man inte ha globala variabler osv
    if Talhantering.lower() != "sqrt":
        Tal2_int = int(input("Tal 2: "))
    else:    
        Tal2_int = None        

    if Talhantering == "*":
        Tal3 = Tal1_int * Tal2_int
    elif Talhantering == "+":
        Tal3 = Tal1_int + Tal2_int
    elif Talhantering == "/":
        Tal3 = Tal1_int / Tal2_int
    elif Talhantering == "-":
        Tal3 = Tal1_int - Tal2_int
    elif Talhantering == "^^":
        Tal3 = Tal1_int ** Tal2_int
    elif Talhantering == "//":
        Tal3 = Tal1_int // Tal2_int
    elif Talhantering.lower() == "sqrt":
        Tal3 = Tal1_int ** 0.5
        
    print (f"Resultatet är: {Tal3}")    


def main():

    print("Välkommen till miniräknaren")
    Talhantering = input("Hur vill du hantera talen? ")
    
    Tal1_int = ratt_raknesatt(Talhantering)
    Tal3 = calculations(Talhantering,Tal1_int) 
    
    if Talhantering.upper() == "/" or "*" or "SQRT":
        Runda = input("Round tal 3?")
        if Runda.upper() == "TRUE":
            print(round(Tal3, 3))


#Visar att Main metoden är main() och att den ska köras först
if __name__ == "__main__":
    main()