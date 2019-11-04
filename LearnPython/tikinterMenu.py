#!/usr/local/bin/python3

# This is tkinter to use with button on frame.

from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("BlueHive Game Center")
        self.pack(fill=BOTH, expand=0)
        #quitButton = Button(self, text ='quit', command=self.client_exit)
        #quitButton.place(x=10, y=10)


        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Save')
        file.add_command(label='SaveAs')
        file.add_command(label='Print')
        file.add_command(label='Convert')
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)


        edit = Menu(menu)
        edit.add_command(label='Undo')
        edit.add_command(label='Redo')
        edit.add_command(label='Delete')
        edit.add_command(label='Find')
        edit.add_command(label='Findall')
        menu.add_cascade(label='Edit', menu=edit)



    def client_exit(self):
        exit()



root = Tk()

root.geometry('400x300')

app = Window(root)

root.mainloop()