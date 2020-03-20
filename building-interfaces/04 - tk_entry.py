# Python 3 - Get Input tkinter program
# Author: J.Smith

# Import tkinter library
from tkinter import *
import tkinter.messagebox as box

# A window
window = Tk()
window.title('Input Entry Example')

# A frame to hold input entry field
frame = Frame(window)
entry = Entry(window)


# A function to display data currently entered
def dialog():
    box.showinfo('Greetings', 'Welcome ' + entry.get())


# Button to call function when clicked
btn = Button(frame, text = 'Enter Name', command = dialog)


# Add button and input to the frame
btn.pack(side = RIGHT, padx = 5)
entry.pack(side = LEFT, padx = 15)
frame.pack(padx = 50, pady = 20)

# Maintain the current window
window.mainloop()
