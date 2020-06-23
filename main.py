from tkinter import *
import numpy as np
import scipy as sc
import matplotlib as plt
from PIL import Image, ImageTk

#button press
def buttonPressed():
    print('button pressed -> loading image')
    image = Image.open("temp.gif")
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    #save photo so garbage collector don't trash it
    label.photo = photo
    label.pack()
    label.place(relx = 0.5, rely = 0.5, anchor = 'center')

#create application and set size
root = Tk()
root.geometry("1000x500")

#add a button
but = Button(root, command = buttonPressed, text = 'button')
but.pack()

#run application
root.mainloop()