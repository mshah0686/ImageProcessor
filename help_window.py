import tkinter.scrolledtext as tkscrolled
from tkinter import *

def help():
    print('Help button pressed')
    help_window = Tk()
    help_window.title('Filter Help')
    help_window.geometry("400x500")

    default_text = '1234'
    width, height = 400, 500
    TKScrollTXT = tkscrolled.ScrolledText(help_window, width=width, height=height, wrap='word')

    # set default text if desired
    TKScrollTXT.insert(1.0, default_text)
    TKScrollTXT.pack(side=LEFT)
    help_window.mainloop()