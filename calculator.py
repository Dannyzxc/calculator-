from tkinter import *

root = Tk()
root.title("Calculator")

enter_data = Entry(root, width=40, borderwidth=5)
enter_data.grid(row=0, column=0, columnspan=3)


def operation():
          current = enter_data.get()
          if '+' in current:
                    ops = current.split('+')
                    num1 = ops[0] 
                    num2 = ops[1] 
                    result = int(num1) + int(num2)
                    enter_data.delete(0,END)
                    enter_data.insert(0,str(result))

          if '-' in current:
                    ops = current.split('-')
                    num1 = ops[0] 
                    num2 = ops[1] 
                    result = int(num1) - int(num2)
                    enter_data.delete(0,END)
                    enter_data.insert(0,str(result))

          if '*' in current:
                    ops = current.split('*')
                    num1 = ops[0] 
                    num2 = ops[1] 
                    result = int(num1) * int(num2)
                    enter_data.delete(0,END)
                    enter_data.insert(0,str(result))

          if '/' in current:
                    ops = current.split('/')
                    num1 = ops[0] 
                    num2 = ops[1] 
                    result = int(num1) / int(num2)
                    enter_data.delete(0,END)
                    enter_data.insert(0,str(result))

          



def clear_data():
          enter_data.delete(0,END)


def btn_click(data):
         

          current = enter_data.get()
          enter_data.delete(0,END)
          enter_data.insert(0,str(current) + str(data))





one = Button(root, text="1", padx=40, pady=20, command=lambda: btn_click(1))
one.grid(row=1, column=0)

two = Button(root, text="2", padx=40, pady=20, command=lambda: btn_click(2))
two.grid(row=1, column=1)

three = Button(root, text="3", padx=40, pady=20, command=lambda: btn_click(3))
three.grid(row=1, column=2)

four = Button(root, text="4", padx=40, pady=20, command=lambda: btn_click(4))
four.grid(row=2, column=0)

five = Button(root, text="5", padx=40, pady=20, command=lambda: btn_click(5))
five.grid(row=2, column=1)

six = Button(root, text="6", padx=40, pady=20, command=lambda: btn_click(6))
six.grid(row=2, column=2)

seven = Button(root, text="7", padx=40, pady=20, command=lambda: btn_click(7))
seven.grid(row=3, column=0)

eight = Button(root, text="8", padx=40, pady=20, command=lambda: btn_click(8))
eight.grid(row=3, column=1)

nine = Button(root, text="9", padx=40, pady=20, command=lambda: btn_click(9))
nine.grid(row=3, column=2)

plus = Button(root, text="+", padx=39, pady=20, command=lambda: btn_click('+'))
plus.grid(row=4, column=0)

zero = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0))
zero.grid(row=4, column=1)


minus = Button(root, text="-", padx=40, pady=20, command=lambda: btn_click("-"))
minus.grid(row=4, column=2)

divide = Button(root, text="/", padx=40, pady=20, command=lambda: btn_click('/'))
divide.grid(row=5, column=2)

multiply = Button(root, text="x", padx=40, pady=20,command=lambda: btn_click('*'))
multiply.grid(row=5, column=0)

clear_btn = Button(root, text="C", padx=40, pady=20,command=clear_data)
clear_btn.grid(row=5, column=1)

equalto = Button(root, text="=", padx=40, pady=20,command=operation)
equalto.grid(row=6, column=0, columnspan=3)


root.mainloop()
