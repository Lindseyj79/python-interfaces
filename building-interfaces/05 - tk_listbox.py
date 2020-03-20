# Python 3 - List Options tkinter program
# Author: J.Smith

# Import tkinter library
from tkinter import *
import tkinter.messagebox as box

# A window
window = Tk()
window.title('Listbox Example')

# A frame to contain widgets
frame = Frame(window)

# Listbox widget - list 3 options
listbox = Listbox(frame)
listbox.insert(1, 'HTML in Easy Steps')
listbox.insert(2, 'CSS in Easy Steps')
listbox.insert(3, 'JavaScript in Easy Steps')


# Function to display the listbox
def dialog():
    box.showinfo('Selection', 'Your choice: ' + listbox.get(listbox.curselection()))


# Button to call function
btn = Button(frame, text = 'Choose', command = dialog)

# Add all to window
btn.pack(side = RIGHT, padx = 5)
listbox.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)

# Maintain the current window
window.mainloop()
