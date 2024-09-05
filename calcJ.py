import tkinter as tk

main = tk.Tk()
main.title("calc")
main.geometry("500x300")

equation = tk.StringVar()

equation_display = tk.Entry(main, textvariable=equation, font=('Arial', 18), justify='right')
equation_display.place(x=50, y=20, width=300, height=50) 

#Till rad 22 (nytt)
def caluculate():
    try: 
        result = eval(equation.get())  # Använd eval för att beräkna uttrycket
        equation.set(result)  # Uppdatera skärmfältet med resultatet
    except Exception as e:
        equation.set("Error")

# Funktion för att hantera knapptryckningar
def button_click(value): 
    current_equation = equation.get()
    equation.set(current_equation + str(value))  # Lägg till tryckt knapp till ekvationen

def clear():
    equation.set("")



#Nya namn har tillagts och andra knappar

button_equals = tk.Button(main,text="=", command=caluculate)
button_equals.place(x=50, y=70, width=50, height=50)
button1 = tk.Button(main,text="1",command=lambda: button_click("1"))
button1.place(x=100, y=70, width=50, height=50)
button2 = tk.Button(main,text="2",command=lambda: button_click("2"))
button2.place(x=150, y=70, width=50, height=50)
button_add = tk.Button(main,text="+",command=lambda: button_click ("+"))
button_add.place(x=50, y=120, width=50, height=50)
button_sub = tk.Button(main,text="-",command=lambda: button_click("-"))
button_sub.place(x=50, y=170, width=50, height=50) 
button_clear = tk.Button(main,text="C",command=lambda: button_click (""))
button_clear.place(x=200, y=170, width=50, height=50)



if __name__ == "__main__": 

    main.mainloop()
