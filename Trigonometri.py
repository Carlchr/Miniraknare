import math

def trig_func():
    while True: 
        trig_list = ["cos", "sin", "tan", "acos", "atan", "asin"]
        if vilken_trig.lower() in trig_list:
            return vilken_trig
        print("Not acceptable")
        vilken_trig = float(input("Vad för trigonometri vill du använda? (cos/sin/tan för sidor)(arccos/arcsin/arctan för vinkel): "))


def calculations():

    if vilken_trig == "arccos":
        
        cosinus = math.acos(nummer_1/nummer_2)
        print(math.degrees(cosinus))
    elif vilken_trig == "arcsin":

        sinus = math.asin(nummer_1/nummer_2)
        print(math.degrees(sinus))

    elif vilken_trig == "arctan":

        tangens = math.atan(nummer_1/nummer_2)
        print(math.degrees(tangens))

    elif vilken_trig == "cos":

        vilken_sida = input("Vilken sida vill du räkna ut? (b/c)")
        vinkel_float = math.radians(float(input("Skriv vinkeln: ")))

        if vilken_sida == "b":

            # Gör om vinkel till float samt radianer så att datorn räknar rätt
            nummer_1 = math.cos(vinkel_float) * nummer_2

            print(f"Svar: {nummer_1}")        
                
        elif vilken_sida == "c":
            
            nnummer_2 = nummer_1 / math.cos(vinkel_float)

            print(f"Svar: {nummer_2}")
        else:
            print("error")

    elif vilken_trig == "sin":

        vilken_sida = input("Vilken sida vill du räkna ut? (a/c)")
        vinkel_float = math.radians(float(input("Skriv vinkeln: ")))


        if vilken_sida == "a":
            
            nummer_1 = math.sin(vinkel_float) * nummer_2
            
            print(f"Svar: {nummer_1}")        
                
        elif vilken_sida == "c":
            
            
            nummer_2 = nummer_1 / math.sin(input(vinkel_float))
            print(f"Svar: {nummer_2}")
        else:
            print("error")

    elif vilken_trig == "tan":
        vilken_sida = input("Vilken sida vill du räkna ut? (b/c)")
        vinkel_float = math.radians(float(input("Skriv vinkeln: ")))
        
        if vilken_sida == "b":

            nummer_2 = nummer_1 / math.tan(vinkel_float) 
            print(f"Svar: {nummer_2}")        
                
        elif vilken_sida == "a":
    
            nummer_1 = nummer_2 * math.tan(vinkel_float)
            print(f"Svar: {nummer_1}")
        else:
            print("error")
    else:
        print("error")


def main():
    vilken_trig = float(input("Vad för trigonometri vill du använda? (cos/sin/tan för sidor)(arccos/arcsin/arctan för vinkel): "))

    nummer_1 = float(input("Tal 1(minsta)(a vid tan): "))
    nummer_2 = float(input("Tal 2(största))(b vid tan): "))
    return nummer_1, nummer_2

if "__name__" == "__main__":
    main()
 


