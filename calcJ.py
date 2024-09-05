import tkinter as tk

main = tk.Tk()
main.title("calc")
main.geometry("400x200")

def caluc():
    print("caluc")
def metod(a,b, Talhantering):
    

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

def val(i):
    print(i)
    




button1 = tk.Button(main,text="=",command=lambda: metod (equation))
button1.place(x=100, y=50, width=50, height=50)
button2 = tk.Button(main,text="1",command=lambda: val("1"))
button2.place(x=150, y=50, width=50, height=50)
button3 = tk.Button(main,text="2",command=lambda: val("2"))
button3.place(x=200, y=50, width=50, height=50)
button4 = tk.Button(main,text="+",command=lambda: val("+"))
button4.place(x=250, y=50, width=50, height=50)
button5 = tk.Button(main,text="-",command=lambda: val("-"))
button5.place(x=250, y=100, width=50, height=50)



if __name__ == "__main__":

    main.mainloop()
