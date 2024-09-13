import tkinter as tk

gui = tk.Tk()
gui.title("Calculator")
gui.geometry("500x700")

#Variabel för att hålla i texten i label 
label_equation = tk.StringVar() 

#texten i label är av variabeln "label_equation"
text_display = tk.Label(gui, textvariable=label_equation, justify="right", font=('Arial', 18))
text_display.place(x = 50, y = 20, width=200, height=40)

def calculate():
    try: #testar om koden ger error
        final_value = eval(label_equation.get())  # Använd eval för att beräkna uttrycket
        label_equation.set(final_value)  # Uppdatera skärmfältet med resultatet
    except Exception as e: #Kombination av value error, syntaxerror och zerodivision error 
        label_equation.set("Error") 


def button_press(value):    
    #Uppdaterad ruta, nuvarande ruta + ny värde(vara säker på att det är en string)
    label_equation.set(label_equation.get() + str(value))

def clear_label():
    #.delete funkar inte på label
    text_display.set("")



#y = 70                                      #Körs vid klick
Button_equals = tk.Button(gui, text="=", command= calculate)
Button_equals.place(height=50, width = 50, x = 50, y = 70)
Button_1 = tk.Button(gui, text="1", command=lambda: button_press("1"))
Button_1.place(height=50, width = 50, x = 100, y = 70)
Button_2 = tk.Button(gui, text="2", command=lambda: button_press("2"))
Button_2.place(height=50, width = 50, x = 150, y = 70)
Button_3 = tk.Button(gui, text="3", command=lambda: button_press("3"))
Button_3.place(height=50, width = 50, x = 200, y = 70)

#y = 120
Button_add = tk.Button(gui, text="+", command=lambda: button_press("+"))
Button_add.place(height=50, width = 50, x = 50, y = 120)
Button_4 = tk.Button(gui, text="4", command=lambda: button_press("4"))
Button_4.place(height=50, width = 50, x = 100, y = 120)
Button_5 = tk.Button(gui, text="5", command=lambda: button_press("5"))
Button_5.place(height=50, width = 50, x = 150, y = 120)
Button_6 = tk.Button(gui, text="6", command=lambda: button_press("6"))
Button_6.place(height=50, width = 50, x = 200, y = 120)

if __name__ == "__main__":
    gui.mainloop()