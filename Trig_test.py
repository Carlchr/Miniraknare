import math

def trig_func(is_side):
    #Array for diffrent functions
    trig_list_side = ["cos", "sin", "tan"]
    trig_list_angle = ["acos", "atan", "asin"]
    
    while True: 
        if is_side: #if you're calculating side, then trig_func(True) = side
            vilken_trig = input("Vad för trigonometri vill du använda? (cos/sin/tan): ") #Input
            if vilken_trig.lower() not in trig_list_side: #checks if the input is the same as th Array
                print("Not acceptable") #If not cos, sin, tan
            else:
                return vilken_trig #if you input cos, sin, tan
        else:
            vilken_trig = input("Vad för trigonometri vill du använda? (acos/asin/atan): ")
            if vilken_trig.lower() not in trig_list_angle:
                print("Not acceptable")
            else:
                return vilken_trig

    #Get the angle and converts it to radians
def get_angle():
    vinkel_float = math.radians(float(input("Skriv vinkeln: ")))
    return vinkel_float

    #Gets the number
def get_number():
    nummer_1 = float(input("Tal 1(minsta)(a vid tan): "))
    nummer_2 = float(input("Tal 2(största))(b vid tan): "))
    return nummer_1, nummer_2

    #Calculating 
def calculations_angle():
    vilken_trig = trig_func(False)
    nummer_1, nummer_2 = get_number()

    #Vanliga uträkningar
    if vilken_trig == "acos":
        cosinus = math.acos(nummer_1/nummer_2)
        print(math.degrees(cosinus))
    elif vilken_trig == "asin":
        sinus = math.asin(nummer_1/nummer_2)
        print(math.degrees(sinus))
    elif vilken_trig == "atan":
        tangens = math.atan(nummer_1/nummer_2)
        print(math.degrees(tangens))
    else:
        print("Error, try again with something else")


def calculations_side():
    vilken_trig = trig_func(True)
    vinkel_float = get_angle()
    nummer_1, nummer_2 = get_number()

    #Vanliga uträkningar
    if vilken_trig == "cos":
        vilken_sida = input("Vilken sida vill du räkna ut? (b/c)")

        if vilken_sida == "b":
            nummer_1 = math.cos(vinkel_float) * nummer_2
            print(f"Svar: {nummer_1}")        
        elif vilken_sida == "c":
            nummer_2 = nummer_1 / math.cos(vinkel_float)
            print(f"Svar: {nummer_2}")
        else:
            print("Error, try again with something else")

    elif vilken_trig == "sin":
        vilken_sida = input("Vilken sida vill du räkna ut? (a/c)")

        if vilken_sida == "a":     
            nummer_1 = math.sin(vinkel_float) * nummer_2
            print(f"Svar: {nummer_1}")                 
        elif vilken_sida == "c":
            nummer_2 = nummer_1 / math.sin(vinkel_float)
            print(f"Svar: {nummer_2}")
        else:
            print("Error, try again with something else")

    elif vilken_trig == "tan":
        vilken_sida = input("Vilken sida vill du räkna ut? (b/c)")
        
        if vilken_sida == "b":
            nummer_2 = nummer_1 / math.tan(vinkel_float) 
            print(f"Svar: {nummer_2}")             
        elif vilken_sida == "a":
            nummer_1 = nummer_2 * math.tan(vinkel_float)
            print(f"Svar: {nummer_1}")
        else:
            print("Error, try again with something else")
    else:
        print("Error, try again with something else")

def main():
    trig_val = input("Vill du räkna ut sida eller vinkel: ").lower()

    if trig_val == "sida" or "side":
        calculations_side()
    elif trig_val == "vinkel" or "angle":
        calculations_angle()
    else:
        print("Error, try again with something else")

if __name__ == "__main__":
    main()


