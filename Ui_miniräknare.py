import tkinter as tk

gui = tk.Tk()
gui.title = ("Calculator")
gui.geometry = ("500x700")

#Variable för 
text_display = tk.StringVar()


def calculate(a, b, talhantering):
    x_float = a
    y_float = b

    if  Talhantering=="+":
        Tal_3 = x_float+y_float
        print(Tal_3)
    elif Talhantering=="-":
        Tal_3 = x_float-y_float
        print(Tal_3)
    elif Talhantering=="/":
        Tal_3 = x_float/y_float
        print(Tal_3)
    elif Talhantering=="*":
        Tal_3 = x_float*y_float
        print(Tal_3)
    elif Talhantering=="//":
        Tal_3 = x_float//y_float
        print(Tal_3)
    elif Talhantering=="**":
        Tal_3 = x_float**y_float
        print(Tal_3)
    elif Talhantering=="sqrt":
        Tal_3 = x_float**0.5
        print(Tal_3)

    Talhantering=input("Round(Tal_3?)")
    if Talhantering=="True":
        print(round(Tal_3, 2))
    elif Talhantering=="False":
        print(Tal_3)
    else:
        print(Tal_3)
'''
def click_button():
def clear():sz
'''
                                                #Körs vid klick
Button_equals = tk.Button(gui, text="=", command=lambda: calculate())
