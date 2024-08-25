Tal1_str = input("Tal 1:")
Tal1_int = int(Tal1_str)
Talhantering = input("Hur vill du hantera talen? ")

if Talhantering != "sqrt": 
    Tal2_str = input("Tal 2: ")
    Tal2_int = int(Tal2_str)

if Talhantering == "*":
    Tal3 = Tal1_int * Tal2_int
    print(Tal3)
elif Talhantering == "+":
    Tal3 = Tal1_int + Tal2_int
    print(Tal3)
elif Talhantering == "/":
    Tal3 = Tal1_int / Tal2_int
    print(Tal3)
elif Talhantering == "-":
    Tal3 = Tal1_int - Tal2_int
    print(Tal3)
elif Talhantering == "^^":
    Tal3 = Tal1_int ** Tal2_int
    print(Tal3)
elif Talhantering == "//":
    Tal3 = Tal1_int // Tal2_int
    print(Tal3)
elif Talhantering == "sqrt":
    Tal3 = Tal1_int ** 0.5
    print(Tal3)
elif Talhantering == "%":
    Tal3 = Tal1_int % Tal2_int
    print(Tal3)
else:
    print("Error")


if Talhantering == "/" or "*" or "sqrt":
    Runda = input("Round tal 3?")
    if Runda.upper() == "TRUE":
        print(round(Tal3, 3))

