from tkinter import *
from tkinter.ttk import *

root = Tk() #begin the app window
root.title("Calculator") #App title

root.resizable(False, False)#makes the window not resizable
#Function_Definitions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    global num1
    global oper
    oper = "+"
    num1=float(e.get())
    e.delete(0, END)

def button_multiply():
    global num1
    global oper
    oper = "*"
    num1=float(e.get())
    e.delete(0, END)

def button_divide():
    global num1
    global oper 
    oper = "/"
    num1=float(e.get())
    e.delete(0, END)

def button_subtract():
    global num1
    global oper
    oper = "-"
    num1=float(e.get())
    e.delete(0, END)

def button_equal():
    
    num2=e.get()
    e.delete(0, END)
    if oper == "+":
        result= float(num1) + float(num2)
    elif oper == "-":
        result= float(num1) - float(num2)
    elif oper == "*":
        result= float(num1) * float(num2)
    elif oper == "/":
        result= float(num1) / float(num2)
    e.insert(0, str(result))



#Entry_Box
e=Entry(root, width = 35)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 5 )
#Button_Definition

#Number_Buttons
but1=Button(root, text = "1", command = lambda:button_click(1))
but2=Button(root, text = "2", command = lambda:button_click(2))
but3=Button(root, text = "3", command = lambda:button_click(3))
but4=Button(root, text = "4", command = lambda:button_click(4))
but5=Button(root, text = "5", command = lambda:button_click(5))
but6=Button(root, text = "6", command = lambda:button_click(6))
but7=Button(root, text = "7", command = lambda:button_click(7))
but8=Button(root, text = "8", command = lambda:button_click(8))
but9=Button(root, text = "9", command = lambda:button_click(9))
but0=Button(root, text = "0", command = lambda:button_click(0))
but_point=Button(root, text = ".", command = lambda:button_click('.'))

#Operation_Buttons
but_add = Button(root, text = "+", command = button_add)
but_subtract = Button(root, text = "-", command = button_subtract)
but_multiply = Button(root, text = "*", command = button_multiply)
but_divide = Button(root, text = "/", command = button_divide)

#Other_Buttons
but_clear = Button(root, text = "C", command = button_clear)
but_equal = Button(root, text = "=",  command = button_equal)

#Button_Implementation
#Button_Numbers
but1.grid(row = 3, column = 0)
but2.grid(row = 3, column = 1)
but3.grid(row = 3, column = 2)

but4.grid(row = 2, column = 0)
but5.grid(row = 2, column = 1)
but6.grid(row = 2, column = 2)

but7.grid(row = 1, column = 0)
but8.grid(row = 1, column = 1)
but9.grid(row = 1, column = 2)

but0.grid(row = 4, column = 1 )
but_point.grid(row = 4, column = 0 )

#Button_Operations
but_add.grid(row = 4, column = 3)
but_multiply.grid(row = 2, column = 3)
but_subtract.grid(row = 3, column = 3)
but_divide.grid(row = 1, column = 3)

#Button_Other
but_clear.grid(row = 0, column = 3)
but_equal.grid(row = 4, column = 2)


root.mainloop()