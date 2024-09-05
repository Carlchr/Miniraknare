import math

def trig_func(is_side):
    trig_list_side = ["cos", "sin", "tan"]
    trig_list_angle = ["acos", "atan", "asin"]
    
    while True: 
        if is_side:
            vilken_trig = input("Vad för trigonometri vill du använda? (cos/sin/tan): ")
            if vilken_trig.lower() not in trig_list_side:
                print("Not acceptable")
            else:
                return vilken_trig
        else:
            vilken_trig = input("Vad för trigonometri vill du använda? (acos/asin/atan): ")
            if vilken_trig.lower() not in trig_list_angle:
                print("Not acceptable")
            else:
                return vilken_trig

def get_angle():
    vinkel_float = math.radians(float(input("Skriv vinkeln: ")))
    return vinkel_float

def calculations_angle():
    vilken_trig = trig_func(False)

    nummer_1 = float(input("Tal 1(minsta)(a vid tan): "))
    nummer_2 = float(input("Tal 2(största)(b vid tan): "))

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
    vilken_trig = trig_func(True)
    vinkel_float = get_angle()
    
    nummer_1 = float(input("Tal 1(minsta)(a vid tan): "))
    nummer_2 = float(input("Tal 2(största)(b vid tan): "))

    if vilken_trig == "cos":
        vilken_sida = input("Vilken sida vill du räkna ut? (b/c)")

        if vilken_sida == "b":
            nummer_1 = math.cos(vinkel_float) * nummer_2
            print(f"Svar: {nummer_1}")        
        elif vilken_sida == "c":
            nummer_2 = nummer_1 / math.cos(vinkel_float)
            print(f"Svar: {nummer_2}")
        else:
            print("Error")

    elif vilken_trig == "sin":
        vilken_sida = input("Vilken sida vill du räkna ut? (a/c)")

        if vilken_sida == "a":     
            nummer_1 = math.sin(vinkel_float) * nummer_2
            print(f"Svar: {nummer_1}")                 
        elif vilken_sida == "c":
            nummer_2 = nummer_1 / math.sin(vinkel_float)
            print(f"Svar: {nummer_2}")
        else:
            print("Error")

    elif vilken_trig == "tan":
        vilken_sida = input("Vilken sida vill du räkna ut? (b/c)")
        
        if vilken_sida == "b":
            nummer_2 = nummer_1 / math.tan(vinkel_float) 
            print(f"Svar: {nummer_2}")             
        elif vilken_sida == "a":
            nummer_1 = nummer_2 * math.tan(vinkel_float)
            print(f"Svar: {nummer_1}")
        else:
            print("Error")
    else:
        print("Error")

def main():
    trig_val = input("Vill du räkna ut sida eller vinkel: ").lower()

    if trig_val == "sida":
        calculations_side()
    elif trig_val == "vinkel":
        calculations_angle()
    else:
        print("Ogilitigt svar, försök igen")

if __name__ == "__main__":
    main()


