import math

def trig_func():
    vilken_trig = main()
    trig_list = ["cos", "sin", "tan", "acos", "atan", "asin"]
    while True: 
        vilken_trig = float(input("Vad för trigonometri vill du använda? (cos/sin/tan för sidor)(arccos/arcsin/arctan för vinkel): "))
        if vilken_trig.lower() not in trig_list:
            print("Not acceptable")
        else:
            return vilken_trig.lower()

def get_angle():
    vinkel_float = math.radians(float(input("Skriv vinkeln: ")))
    return vinkel_float

def calculations_angle():
    vilken_trig = trig_func()
    nummer_1 = main()
    nummer_2 = main()


    if vilken_trig == "acos":
        cosinus = math.acos(nummer_1/nummer_2)
        print(math.degrees(cosinus))
    elif vilken_trig == "asin":
        sinus = math.asin(nummer_1/nummer_2)
        print(math.degrees(sinus))
    elif vilken_trig == "atan":
        tangens = math.atan(nummer_1/nummer_2)
        print(math.degrees(tangens))


def calculations_side():
    #Hämtar vilken_trig
    vilken_trig = trig_func()

    if vilken_trig == "cos":
        vilken_sida = input("Vilken sida vill du räkna ut? (b/c)")
        vinkel_float = get_angle()

        if vilken_sida == "b":
            # Gör om vinkel till float samt radianer så att datorn räknar rätt
            nummer_1 = math.cos(vinkel_float) * nummer_2
            print(f"Svar: {nummer_1}")        
        elif vilken_sida == "c":
            nummer_2 = nummer_1 / math.cos(vinkel_float)
            print(f"Svar: {nummer_2}")
        else:
            print("error")

    elif vilken_trig == "sin":

        vilken_sida = input("Vilken sida vill du räkna ut? (a/c)")
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

    vilken_trig = trig_func(vilken_trig)

    nummer_1 = float(input("Tal 1(minsta)(a vid tan): "))
    nummer_2 = float(input("Tal 2(största))(b vid tan): "))
    return nummer_1, nummer_2

    calculations_angle(vilken_trig, number_1, number_2)
    calculations_side(vilken_trig, number_1, number_2)


if "__name__" == "__main__":
    main()
 


