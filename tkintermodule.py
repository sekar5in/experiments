#!/usr/local/bin/python3

# This is basic GUI window creation using tkinter module.

from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

root = Tk()
app = Window(root)
root.mainloop()