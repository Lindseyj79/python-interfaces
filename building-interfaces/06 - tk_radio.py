# Python 3 - Polling radio buttons tkinter program
# Author: J.Smith

# Import tkinter library
from tkinter import *
import tkinter.messagebox as box

# A window
window = Tk()
window.title('Radio Button Example')

# Frame to contain widgets
frame = Frame(window)

# String variable to store a selection
book = StringVar()

# Three radio button widgets
radio_1 = Radiobutton(frame, text = "HTML5", variable = book, value = "HTML5 in Easy Steps")
radio_2 = Radiobutton(frame, text = "CSS", variable = book, value = "CSS in Easy Steps")
radio_3 = Radiobutton(frame, text = "JS", variable = book, value = "JavaScript in Easy Steps")

# Set default radio button
radio_1.select()


# Function to show selection
def dialog():
    box.showinfo('Selection', 'Your choice: \n' + book.get())


# Button to run the function
btn = Button(frame, text = "Choose", command = dialog)

# Pack all the elements together
btn.pack(side = RIGHT, padx = 5)
radio_1.pack(side = LEFT)
radio_2.pack(side = LEFT)
radio_3.pack(side = LEFT)
frame.pack(padx = 30, pady= 30)

# Maintain the current window
window.mainloop()