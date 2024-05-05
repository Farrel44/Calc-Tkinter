from tkinter import * # type: ignore

equation_text = ""

def button_press(num):
    
    global equation_text
    
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    
    try: 
        total = str(eval(equation_text))
        
        equation_label.set(total)
        
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Error Aritmatik")
        
        equation_text = ""
    except SyntaxError:
        equation_label.set("Error Syntax")
        
        equation_text = ""

def clear():
    global equation_text 
    
    equation_label.set("")
    equation_text = ""
    
def erase():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)

window = Tk()
window.title("Calculator")
window.geometry("400x530")
window.config(bg="#222831")
window.resizable(False, False)

equation = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("Arial", 26, 'bold'), bg="#414660", fg="#45878A",width=24, height=2, anchor='e')
label.pack()

frame = Frame(window, bg="#222831")
frame.pack()

btn7 = Button(frame, text=7, height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#31363F",command=lambda: button_press(7))
btn7.grid(row=1, column=0)
btn8 = Button(frame, text=8, height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#31363F",command=lambda: button_press(8))
btn8.grid(row=1, column=1)
btn9 = Button(frame, text=9, height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#31363F",command=lambda: button_press(9))
btn9.grid(row=1, column=2)
btn4 = Button(frame, text=4, height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#31363F",command=lambda: button_press(4))
btn4.grid(row=2, column=0)
btn5 = Button(frame, text=5, height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#31363F",command=lambda: button_press(5))
btn5.grid(row=2, column=1)
btn6 = Button(frame, text=6, height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#31363F",command=lambda: button_press(6))
btn6.grid(row=2, column=2)
btn1 = Button(frame, text=1, height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#31363F",command=lambda: button_press(1))
btn1.grid(row=3, column=0)
btn2 = Button(frame, text=2, height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#31363F",command=lambda: button_press(2))
btn2.grid(row=3, column=1)
btn3 = Button(frame, text=3, height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#31363F",command=lambda: button_press(3))
btn3.grid(row=3, column=2)

btn0 = Button(frame, text=0, height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#31363F",command=lambda: button_press(0))
btn0.grid(row=4, column=0)
btnPlus = Button(frame, text='+', height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#45878A",command=lambda: button_press('+'))
btnPlus.grid(row=0, column=3)
btnMinus = Button(frame, text='-', height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#45878A",command=lambda: button_press('-'))
btnMinus.grid(row=1, column=3)
btnMult = Button(frame, text='x', height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#45878A",command=lambda: button_press('*'))
btnMult.grid(row=2, column=3)
btnDivide = Button(frame, text='/', height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#45878A",command=lambda: button_press('/'))
btnDivide.grid(row=3, column=3)
btnEqual = Button(frame, text='=', height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#414660",command=equals)
btnEqual.grid(row=4, column=3)

btnErase = Button(frame, text='⌫', height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#414660",command=erase)
btnErase.grid(row=4, column=2)

btnClear = Button(frame, text='Clear', height=3, width=15, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#5D9A77",command=clear)
btnClear.grid(row=0, column=0, columnspan=2)

btnExponent = Button(frame, text='^', height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#45878A",command=lambda: button_press("**"))
btnExponent.grid(row=0, column=2)

btnDecimal = Button(frame, text='.', height=3, width=7, font=("Arial", 16, "bold"), fg="#EEEEEE", bg="#31363F",command=lambda:button_press('.'))
btnDecimal.grid(row=4, column=1)













window.mainloop()



