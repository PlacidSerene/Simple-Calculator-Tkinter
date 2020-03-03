from tkinter import *

root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=35,borderwidth=5)
e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
   
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add(operator):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + (operator))

def button_subtract(operator):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + (operator))

def button_multiply(operator):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + (operator))

def button_divide(operator):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + (operator))
# 7+8
def button_equal():
    current = e.get()
    e.delete(0, END)
    if "x" in current:
        current = current.replace("x", '*')
    if ":" in current:
        current = current.replace(":", '/')
    e.insert(0, eval(current))

##define button
Button7 = Button(root, text="7", fg="blue", bg="#ffd3b6", padx=40, pady=20, command=lambda: button_click(7))
Button8 = Button(root, text="8", fg="blue", bg="#ffd3b6", padx=40, pady=20, command=lambda: button_click(8))
Button9 = Button(root, text="9", fg="blue", bg="#ffd3b6", padx=40, pady=20, command=lambda: button_click(9))
Button4 = Button(root, text="4", fg="blue", bg="#ffd3b6", padx=40, pady=20, command=lambda: button_click(4))
Button5 = Button(root, text="5", fg="blue", bg="#ffd3b6", padx=40, pady=20, command=lambda: button_click(5))
Button6 = Button(root, text="6", fg="blue", bg="#ffd3b6", padx=40, pady=20, command=lambda: button_click(6))
Button1 = Button(root, text="1", fg="blue", bg="#ffd3b6", padx=40, pady=20, command=lambda: button_click(1))
Button2 = Button(root, text="2", fg="blue", bg="#ffd3b6", padx=40, pady=20, command=lambda: button_click(2))
Button3 = Button(root, text="3", fg="blue", bg="#ffd3b6", padx=40, pady=20, command=lambda: button_click(3))
Button0 = Button(root, text="0", fg="blue", bg="#ffd3b6", padx=40, pady=20, command=lambda: button_click(0))
ButtonAdd = Button(root, text="+", fg="blue", bg="#e8f9e9", padx=40, pady=20, command=lambda: button_add("+"))
ButtonEqual = Button(root, text="=", fg="blue", bg="#e8f9e9", padx=39, pady=20, command=button_equal)
ButtonClear = Button(root, text="Clear", fg="blue", bg="#e8f9e9", padx=127, pady=20, command=button_clear)
ButtonSubtract = Button(root, text="-", fg="blue", bg="#e8f9e9", padx=40, pady=20, command=lambda: button_subtract("-"))
ButtonMultiply = Button(root, text="x", fg="blue", bg="#e8f9e9", padx=40, pady=20, command=lambda: button_multiply("x"))
ButtonDivide = Button(root, text=":", fg="blue", bg="#e8f9e9", padx=42, pady=20, command=lambda: button_divide(":"))


#put button on the screen
Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)
Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)
Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)
Button0.grid(row=4, column=0)
ButtonAdd.grid(row=4, column=1, columnspan=1)
ButtonSubtract.grid(row=4, column=2, columnspan=1)
ButtonMultiply.grid(row=5, column=0, columnspan=1)
ButtonDivide.grid(row=5, column=1, columnspan=1)
ButtonEqual.grid(row=5, column=2, columnspan=1)
ButtonClear.grid(row=6, column=0, columnspan=3)
root.mainloop()

# current = "3 x 5"
# current = current.replace("x", '*')
# print(eval(current))