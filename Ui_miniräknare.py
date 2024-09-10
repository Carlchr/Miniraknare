import tkinter as tk

gui = tk.Tk()
gui.title = ("Calculator")
gui.geometry = ("500x700")

#Variable för 
text_display = tk.StringVar() 

def calculate(a, b, Talhantering):
    x_float = a
    y_float = b

    Talhantering = input("Vilket räknesätt")

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

                                                #Körs vid klick
Button_equals = tk.Button(gui, text="=", command=lambda: calculate)
Button_equals.place(height=50, width = 50, x = 50, y = 50)
Button_1 = tk.Button(gui, text="1", command=lambda: (1))
Button_1.place(height=50, width = 50, x = 100, y = 50)
Button_2 = tk.Button(gui, text="2", command=lambda: (2))
Button_2.place(height=50, width = 50, x = 100, y = 50)
Button_3 = tk.Button(gui, text="3", command=lambda: (3))
Button_3.place(height=50, width = 50, x = 100, y = 50)
Button_4 = tk.Button(gui, text="4", command=lambda: (4))
Button_4.place(height=50, width = 50, x = 150, y = 50)
Button_5 = tk.Button(gui, text="5", command=lambda: (5))
Button_5.place(height=50, width = 50, x = 150, y = 100)


if __name__ == "__main__":
    gui.mainloop()