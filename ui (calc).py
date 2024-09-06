import tkinter as tk

main = tk.Tk()
main.title("calculator")
main.geometry("500x300")

equation = tk.StringVar()

equation_display = tk.Entry(main, textvariable=equation, font=('Arial', 18), justify='right')
equation_display.place(x=50, y=20, width=300, height=50) 

#Till rad 27 (nytt)
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

def clear_text():
    equation_display.delete(0, tk.END)


#Nya namn har tillagts och andra knappar

button_equals = tk.Button(main,text="=", command=caluculate)
button_equals.place(x=200, y=220, width=50, height=50)
button_1 = tk.Button(main,text="1",command=lambda: button_click("1"))
button_1.place(x=100, y=170, width=50, height=50)
button_2 = tk.Button(main,text="2",command=lambda: button_click("2"))
button_2.place(x=150, y=170, width=50, height=50)
button_3 = tk.Button(main,text="3",command=lambda: button_click("3"))
button_3.place(x=200, y=170, width=50, height=50)
button_4 = tk.Button(main,text="4",command=lambda: button_click("4"))
button_4.place(x=100, y=120, width=50, height=50)
button_5 = tk.Button(main,text="5",command=lambda: button_click("5"))
button_5.place(x=150, y=120, width=50, height=50)
button_6 = tk.Button(main,text="6",command=lambda: button_click("6"))
button_6.place(x=200, y=120, width=50, height=50)
button_7 = tk.Button(main,text="7",command=lambda: button_click("7"))
button_7.place(x=100, y=70, width=50, height=50)
button_8 = tk.Button(main,text="8",command=lambda: button_click("8"))
button_8.place(x=150, y=70, width=50, height=50)
button_9 = tk.Button(main,text="9",command=lambda: button_click("9"))
button_9.place(x=200, y=70, width=50, height=50)
button_0 = tk.Button(main,text="0",command=lambda: button_click("0"))
button_0.place(x=150, y=220, width=50, height=50)
button_add = tk.Button(main,text="+",command=lambda: button_click ("+"))
button_add.place(x=50, y=70, width=50, height=50)
button_sub = tk.Button(main,text="-",command=lambda: button_click("-"))
button_sub.place(x=50, y=120, width=50, height=50) 
button_multi = tk.Button(main,text="*",command=lambda: button_click("*"))
button_multi.place(x=50, y=170, width=50, height=50) 
button_div = tk.Button(main,text="/",command=lambda: button_click("/"))
button_div.place(x=50, y=220, width=50, height=50) 
button_clear = tk.Button(main,text="C", command=clear_text)
button_clear.place(x=100, y=220, width=50, height=50) 

if __name__ == "__main__": 

    main.mainloop()
