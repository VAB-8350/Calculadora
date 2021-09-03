# >>>Victor Andres Barilin<<<
from calculadore import calculation, notation
from tkinter import *

root = Tk()
root.title('calculator')

display = Entry(root)
display.grid(row = 0, columnspan=6, sticky = W+E)

nota = Entry(root)
nota.grid(row = 6, columnspan=6, sticky = W+E)
nota.insert(0, '      >separe los elementos<')

i = 0

def get_numbers(n):
    global i
    display.insert(i, n)
    i += 1

def get_operator(operador):
    global i
    lengt = len(operador)
    display.insert(i, operador)
    i += lengt

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()

def calculate():
    display_state = str(display.get())
    notacion = notation(display_state)
    try:
        result = calculation(display_state, notacion)
        clear_display()
        display.insert(0, result)
        nota.delete(0, END)
        nota.insert(0, 'Notacion: '+notacion)
    except:
        clear_display()
        display.insert(0, 'Error')
        nota.delete(0, END)
        nota.insert(0, 'Error')

#notones numericos
Button(root, text='1', command = lambda:get_numbers(1)).grid(row = 1, column = 0, sticky = W+E)
Button(root, text='2', command = lambda:get_numbers(2)).grid(row = 1, column = 1, sticky = W+E)
Button(root, text='3', command = lambda:get_numbers(3)).grid(row = 1, column = 2, sticky = W+E)

Button(root, text='4', command = lambda:get_numbers(4)).grid(row = 2, column = 0, sticky = W+E)
Button(root, text='5', command = lambda:get_numbers(5)).grid(row = 2, column = 1, sticky = W+E)
Button(root, text='6', command = lambda:get_numbers(6)).grid(row = 2, column = 2, sticky = W+E)

Button(root, text='7', command = lambda:get_numbers(7)).grid(row = 3, column = 0, sticky = W+E)
Button(root, text='8', command = lambda:get_numbers(8)).grid(row = 3, column = 1, sticky = W+E)
Button(root, text='9', command = lambda:get_numbers(9)).grid(row = 3, column = 2, sticky = W+E)

#botones de funciones
Button(root, text='.', command = lambda:get_operator('.')).grid(row = 4, column = 0, sticky = W+E)
Button(root, text='AC', command = lambda:clear_display()).grid(row = 2, column = 5, sticky = W+E)
Button(root, text='0', command = lambda:get_numbers(0)).grid(row = 4, column = 1, sticky = W+E)

Button(root, text='+', command = lambda:get_operator('+')).grid(row = 1, column = 3, sticky = W+E)
Button(root, text='-', command = lambda:get_operator('-')).grid(row = 2, column = 3, sticky = W+E)
Button(root, text='*', command = lambda:get_operator('*')).grid(row = 3, column = 3, sticky = W+E)
Button(root, text='/', command = lambda:get_operator('/')).grid(row = 2, column = 4, sticky = W+E)

Button(root, text='←', command = lambda:undo()).grid(row = 1, column = 4, sticky = W+E, columnspan = 2)
Button(root, text='(', command = lambda:get_operator('(')).grid(row = 3, column = 4, sticky = W+E)
Button(root, text=')', command = lambda:get_operator(')')).grid(row = 3, column = 5, sticky = W+E)
Button(root, text='=', command = lambda:calculate()).grid(row = 4, column = 4, sticky = W+E, columnspan = 2)
Button(root, text='͟', command = lambda:get_operator(' ')).grid(row = 4, column = 2, sticky = W+E, columnspan = 2)
root.mainloop()