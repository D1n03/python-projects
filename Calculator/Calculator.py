from tkinter import *

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
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

def do_sqrt():
    global equation_text
    equation_text = str(float(equation_label.get()) ** 0.5)
    equation_label.set(equation_text)

def do_pow():
    global equation_text
    equation_text = str(float(equation_label.get()) ** 2)
    equation_label.set(equation_text)

def do_xdiv():
    global equation_text
    equation_text = str(1/float(equation_label.get()))
    equation_label.set(equation_text)

#ADD sqrt and 1/x and pow

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculator")
window.geometry("400x550")
window['background'] = '#1F1F1F'
icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable = equation_label, font = ('TimeNewRoman', 20), bg ='#1F1F1F', width = 26, height = 2, highlightbackground='white', highlightthickness=3, foreground='white')
label.pack()

frame = Frame(window)
frame.pack()

percentbutton = Button(frame, text = '1/x', height = 4, width = 9, font = 35, command = do_xdiv, bg = '#060606', foreground='white')
percentbutton.grid(row = 0, column = 0)

powbutton = Button(frame, text = 'x²', height = 4, width = 9, font = 35, command = do_pow, bg = '#060606', foreground='white')
powbutton.grid(row = 0, column = 1)

sqrtbutton = Button(frame, text = '√x', height = 4, width = 9, font = 35, command = do_sqrt, bg = '#060606', foreground='white')
sqrtbutton.grid(row = 0, column = 2)

clear = Button(frame, text = 'clear', height = 4, width = 9, font = 35, command = clear, bg = '#060606', foreground='white')
clear.grid(row = 0, column = 3)

button7 = Button(frame, text = 7, height = 4, width = 9, font = 35, command = lambda: button_press(7), bg = '#060606', foreground='white')
button7.grid(row = 1, column = 0)

button8 = Button(frame, text = 8, height = 4, width = 9, font = 35, command = lambda: button_press(8), bg = '#060606', foreground='white')
button8.grid(row = 1, column = 1)

button9 = Button(frame, text = 9, height = 4, width = 9, font = 35, command = lambda: button_press(9), bg = '#060606', foreground='white')
button9.grid(row = 1, column = 2)

divide = Button(frame, text = '/', height = 4, width = 9, font = 35, command = lambda: button_press('/'), bg = '#060606', foreground='white')
divide.grid(row = 1, column = 3)

button4 = Button(frame, text = 4, height = 4, width = 9, font = 35, command = lambda: button_press(4), bg = '#060606', foreground='white')
button4.grid(row = 2, column = 0)

button5 = Button(frame, text = 5, height = 4, width = 9, font = 35, command = lambda: button_press(5), bg = '#060606', foreground='white')
button5.grid(row = 2, column = 1)

button6 = Button(frame, text = 6, height = 4, width = 9, font = 35, command = lambda: button_press(6), bg = '#060606', foreground='white')
button6.grid(row = 2, column = 2)

multiply = Button(frame, text = '*', height = 4, width = 9, font = 35, command = lambda: button_press('*'), bg = '#060606', foreground='white')
multiply.grid(row = 2, column = 3)

button1 = Button(frame, text = 1, height = 4, width = 9, font = 35, command = lambda: button_press(1), bg = '#060606', foreground='white')
button1.grid(row = 3, column = 0)

button2 = Button(frame, text = 2, height = 4, width = 9, font = 35, command = lambda: button_press(2), bg = '#060606', foreground='white')
button2.grid(row = 3, column = 1)

button3 = Button(frame, text = 3, height = 4, width = 9, font = 35, command = lambda: button_press(3), bg = '#060606', foreground='white')
button3.grid(row = 3, column = 2)

minus = Button(frame, text = '-', height = 4, width = 9, font = 35, command = lambda: button_press('-'), bg = '#060606', foreground='white')
minus.grid(row = 3, column = 3)

button0 = Button(frame, text = 0, height = 4, width = 9, font = 35, command = lambda: button_press(0), bg = '#060606', foreground='white')
button0.grid(row = 4, column = 0)

decimal = Button(frame, text = '.', height = 4, width = 9, font = 35, command = lambda: button_press('.'), bg = '#060606', foreground='white')
decimal.grid(row = 4, column = 1)

equal = Button(frame, text = '=', height = 4, width = 9, font = 35, command = equals, bg = '#060606', foreground='white')
equal.grid(row = 4, column = 2)

plus = Button(frame, text = '+', height = 4, width = 9, font = 35, command = lambda: button_press('+'), bg = '#060606', foreground='white')
plus.grid(row = 4, column = 3)

window.mainloop()