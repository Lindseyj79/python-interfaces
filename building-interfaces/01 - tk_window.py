# Python 3 - Window tkinter program
# Author: J.Smith

# Import tkinter library
from tkinter import *

# Create a tkinter window
window = Tk()
# Set window title
window.title('Label Example')
# Set window size
window.geometry('500x500')

# Create a label
label = Label(window, text = 'Hello World!')
# Add label to window
label.pack(padx = 200, pady = 50)

# Maintains the window
window.mainloop()



