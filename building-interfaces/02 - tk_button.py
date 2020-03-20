# Python 3 - Button tkinter program
# Author: J.Smith

# Import tkinter library
from tkinter import *
import webbrowser

# Create a window
window = Tk()
window.title('Button Example')

# Create a close button
btn_close = Button(window, text = 'Close', command = exit)


# Function for btn_tog
def tog():
    # Retrieve bg color of window
    if window.cget('bg') == 'yellow':
        # Configure the bg color
        window.configure(bg = 'gray')
    else:
        # Configure the bg color
        window.configure(bg = 'yellow')


# Create a toggle button
btn_tog = Button(window, text = 'Switch', command = tog)

# Add both buttons using pack geometry manager
btn_close.pack(padx = 150, pady = 50)
btn_tog.pack(padx = 150, pady = 50)

# Maintain the current window
window.mainloop()

