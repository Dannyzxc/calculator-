from tkinter import *

root = Tk()
root.title("Calculator")

enter_data = Entry(root, width=40, borderwidth=5)
enter_data.grid(row=0, column=0, columnspan=3)



          
def btn_add():
          first_number =  enter_data.get()
          global f_num
          global ops
          ops = "add"
          f_num = int(first_number)
          enter_data.delete(0,END)

          
def btn_divide():
          first_number =  enter_data.get()
          global f_num
          global ops
          ops = "divide"
          f_num = int(first_number)
          enter_data.delete(0,END)

          
def btn_sub():
          first_number =  enter_data.get()
          global f_num
          global ops
          ops = "sub"
          f_num = int(first_number)
          enter_data.delete(0,END)

          
def btn_multiply():
          first_number =  enter_data.get()
          global f_num
          global ops
          ops = "multiply"
          f_num = int(first_number)
          enter_data.delete(0,END)


def clear_data():
          enter_data.delete(0,END)


def btn_equal():
          secand_num =  enter_data.get()
          enter_data.delete(0,END)

          if ops == "add":
                    enter_data.insert(0,f_num + int(secand_num))

          if ops == "sub":
                    enter_data.insert(0,f_num - int(secand_num))

          if ops == "multiply":
                    enter_data.insert(0,f_num * int(secand_num))

          if ops == "divide":
                    enter_data.insert(0,f_num / int(secand_num))


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

add = Button(root, text="+", padx=39, pady=20, command=btn_add)
add.grid(row=4, column=0)

zero = Button(root, text="0", padx=40, pady=20, command=lambda: btn_click(0))
zero.grid(row=4, column=1)


sub = Button(root, text="-", padx=40, pady=20, command=btn_sub)
sub.grid(row=4, column=2)

divide = Button(root, text="/", padx=40, pady=20, command=btn_divide)
divide.grid(row=5, column=2)

multiply = Button(root, text="x", padx=40, pady=20,command=btn_multiply)
multiply.grid(row=5, column=0)

clear_btn = Button(root, text="C", padx=40, pady=20,command=clear_data)
clear_btn.grid(row=5, column=1)

equalto = Button(root, text="=", padx=40, pady=20,command=btn_equal)
equalto.grid(row=6, column=0, columnspan=3)


root.mainloop()
