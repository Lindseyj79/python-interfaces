# Python 3 - Checking checkboxes tkinter program
# Author: J.Smith

# Import tkinter library
from tkinter import *
import tkinter.messagebox as box

# A window
window = Tk()
window.title('Check Button Example')

# Frame to contain widgets
frame = Frame(window)

# Construct 3 variable objects to store values
var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()

# 3 checkboxes which will store values either 1 or 0
book_1 = Checkbutton(frame, text = 'HTML5', variable = var_1, onvalue = 1, offvalue = 0)
book_2 = Checkbutton(frame, text = 'CSS', variable = var_2, onvalue = 1, offvalue = 0)
book_3 = Checkbutton(frame, text = 'JS', variable = var_3, onvalue = 1, offvalue = 0)


# Function to display checkbox selection
def dialog():
    str = 'Your Choice:'
    if var_1.get() == 1: str += '\nHTML5 in Easy Steps'
    if var_2.get() == 1: str += '\nCSS in Easy Steps'
    if var_3.get() == 1: str += '\nJavaScript in Easy Steps'
    box.showinfo('Selection', str)


# Button to call the function
btn = Button(frame, text = 'Choose', command = dialog)

# Add all elements together
btn.pack(side = RIGHT, padx = 5)
book_1.pack(side = LEFT)
book_2.pack(side = LEFT)
book_3.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)

# Maintain the current window
window.mainloop()
