# Python 3 - Message tkinter program
# Author: J.Smith

# Import tkinter library
from tkinter import *
import tkinter.messagebox as box

# Create a window
window = Tk()
window.title('Message Box Example')


# Function to display various message boxes
def dialog():
    var = box.askyesno('Message Box', 'Proceed?')
    if var == 1:
        box.showinfo('Yes Box', 'Proceeding...')
    else:
        box.showwarning('No Box', 'Cancelling...')


# Create a button
btn = Button(window, text = 'Click', command = dialog)
btn.pack(padx = 150, pady = 50)

# Maintain the current window
window.mainloop()
