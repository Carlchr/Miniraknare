import math

Vilken_trig = input("Vad för trigonometri vill du använda? (cos/sin/tan för sidor)(arccos/arcsin/arctan för vinkel): ")

if Vilken_trig == "arccos":
    Tal_b_str = input("skriv tal b: ")
    Tal_b_float = float(Tal_b_str)

    Tal_c_str = input("skriv tal c: ")
    Tal_c_float = float(Tal_c_str)

    cosinus = math.acos(Tal_b_float/Tal_c_float)
    print(math.degrees(cosinus))
elif Vilken_trig == "arcsin":
    Tal_a_str = input("skriv tal a: ")
    Tal_a_float = float(Tal_a_str)

    Tal_c_str = input("skriv tal c: ")
    Tal_c_float = float(Tal_c_str)

    sinus = math.asin(Tal_a_float/Tal_c_float)
    print(math.degrees(sinus))
elif Vilken_trig == "arctan":
    Tal_a_str = input("skriv tal a: ")
    Tal_a_float = float(Tal_a_str)

    Tal_b_str = input("skriv tal b: ")
    Tal_b_float = float(Tal_b_str)

    tangens = math.atan(Tal_a_float/Tal_b_float)
    print(math.degrees(tangens))
elif Vilken_trig == "cos":
    Vilken_sida = input("Vilken sida vill du räkna ut? (b/c)")
    if Vilken_sida == "b":
        Vinkel_str = input("Skriv vinkeln: ")
        # Gör om vinkel till float samt radianer så att datorn räknar rätt
        Vinkel_float = math.radians(float(Vinkel_str))
        Tal_c_float = float(input("skriv tal c: "))

        Tal_b_float = math.cos(Vinkel_float) * Tal_c_float
        print(f"Svar: {Tal_b_float}")        
            
    elif Vilken_sida == "c":
        Vinkel_str = input("Skriv vinkeln: ")
        Vinkel_float = math.radians(float(Vinkel_str))

        Tal_b_float = float(input("skriv tal b: "))

        Tal_c_float = Tal_b_float / math.cos(Vinkel_float)
        print(f"Svar: {Tal_c_float}")
    else:
        print("error")  
elif Vilken_trig == "sin":
    Vilken_sida = input("Vilken sida vill du räkna ut? (a/c)")
    if Vilken_sida == "a":
        Vinkel_str = input("Skriv vinkeln: ")
        # Gör om vinkel till float samt radianer så att datorn räknar rätt
        Vinkel_float = math.radians(float(Vinkel_str))
        Tal_c_float = float(input("skriv tal c: "))

        Tal_a_float = math.sin(Vinkel_float) * Tal_c_float
        print(f"Svar: {Tal_a_float}")        
            
    elif Vilken_sida == "c":
        Vinkel_str = input("Skriv vinkeln: ")
        Vinkel_float = math.radians(float(Vinkel_str))

        Tal_a_float = float(input("skriv tal a: "))

        Tal_c_float = Tal_a_float / math.sin(Vinkel_float)
        print(f"Svar: {Tal_c_float}")
    else:
        print("error")
elif Vilken_trig == "tan":
    Vilken_sida = input("Vilken sida vill du räkna ut? (b/c)")
    if Vilken_sida == "b":
        Vinkel_str = input("Skriv vinkeln: ")
        # Gör om vinkel till float samt radianer så att datorn räknar rätt
        Vinkel_float = math.radians(float(Vinkel_str))
        Tal_a_float = float(input("skriv tal a: "))

        Tal_b_float = Tal_a_float / math.tan(Vinkel_float) 
        print(f"Svar: {Tal_b_float}")        
            
    elif Vilken_sida == "a":
        Vinkel_str = input("Skriv vinkeln: ")
        Vinkel_float = math.radians(float(Vinkel_str))

        Tal_b_float = float(input("skriv tal b: "))

        Tal_a_float = Tal_b_float * math.tan(Vinkel_float)
        print(f"Svar: {Tal_a_float}")
    else:
        print("error")
else:
    print("error")
