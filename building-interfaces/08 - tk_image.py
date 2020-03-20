# Python 3 - Adding images tkinter program
# Author: J.Smith

# Import tkinter library
from tkinter import *

# A window
window = Tk()
window.title('Image Example')

# Image object from local file
img = PhotoImage(file = 'imgs/py-icon.png')

# Label object to create a yellow background
label = Label(window, image = img, bg = 'yellow')

# Half size of same image
small_img = PhotoImage.subsample(img, x = 2, y =2)

# Button with display as the small image
btn = Button(window, image = small_img)

# Text field to be embedded into the image
txt = Text(window, width = 25, height = 7)
txt.image_create('1.0', image = small_img)
txt.insert('1.1', 'Python Fun!')

# A canvas to hold the image and paint a diagonal line through the image
can = Canvas(window, width = 100, height = 100, bg = 'cyan')
can.create_image((50, 50), image = small_img)
can.create_line(0, 0, 100, 100, width = 25, fill = 'yellow')

# Add widgets to window
label.pack(side = TOP)
btn.pack(side = LEFT, padx = 10)
txt.pack(side = LEFT)
can.pack(side = LEFT, pady = 10)

# Maintain the current window
window.mainloop()