# Python 3 - Lotto tkinter program
# Author: J.Smith

# Widgets:
from tkinter import *
from random import sample

# Initialise window object
window = Tk()
img = PhotoImage(file='imgs/lotto-icon.png')

# Create all necessary widgets
imgLbl = Label(window, image=img)
lbl1 = Label(window, relief='groove', width=4, height=2)
lbl2 = Label(window, relief='groove', width=4, height=2)
lbl3 = Label(window, relief='groove', width=4, height=2)
lbl4 = Label(window, relief='groove', width=4, height=2)
lbl5 = Label(window, relief='groove', width=4, height=2)
lbl6 = Label(window, relief='groove', width=4, height=2)
getBtn = Button(window)
resBtn = Button(window)

# Add widgets using the grid layout
imgLbl.grid(row=1, column=1, rowspan=2, padx=10)
lbl1.grid(row=1, column=2, padx=10, pady=15)
lbl2.grid(row=1, column=3, padx=10)
lbl3.grid(row=1, column=4, padx=10)
lbl4.grid(row=1, column=5, padx=10)
lbl5.grid(row=1, column=6, padx=10)
lbl6.grid(row=1, column=7, padx=10)
getBtn.grid(row=2, column=2, columnspan=4)
resBtn.grid(row=2, column=6, columnspan=2)

# Static Properties:
window.title('Lotto Number Picker')
window.resizable(0, 0)  # Disable windows resize button
getBtn.configure(text="Get my Lucky Numbers!")
resBtn.configure(text="Reset!")


# Initial text for Labels
def resetlbl():
    lbl1.configure(text='...')
    lbl2.configure(text='...')
    lbl3.configure(text='...')
    lbl4.configure(text='...')
    lbl5.configure(text='...')
    lbl6.configure(text='...')


# Initial Properties:
resetlbl()
resBtn.configure(state=DISABLED)


# Function to generate 6 random numbers and assign to labels and enabled the reset button
def pick():
    nums = sample(range(1, 49), 6)
    lbl1.configure(text=nums[0])
    lbl2.configure(text=nums[1])
    lbl3.configure(text=nums[2])
    lbl4.configure(text=nums[3])
    lbl5.configure(text=nums[4])
    lbl6.configure(text=nums[5])
    getBtn.configure(state=DISABLED)
    resBtn.configure(state=NORMAL)


# Function to reset the labels and reset the buttons
def reset():
    resetlbl()
    getBtn.configure(state=NORMAL)
    resBtn.configure(state=DISABLED)


getBtn.configure(command=pick)
resBtn.configure(command=reset)

# Sustain window
window.mainloop()
