# Python Version 3.9.7
#
# Author:        Spencer Davis
#
# Purpose:       Phonebook demo. Demonstrating OOP, Tkinter, GUI Module,
#                using TKinter parent and child relationships
#
# Tested OS:     This code was written and tested to work with Windows 11

from tkinter import *
import tkinter as tk

# Be sure to import our other modules
# so we can have access so them
import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, width)
        self.master.maxsize(500,300)
        #This centerWindow method will center our app on the users screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        #This protocol method is a tkinter built in method to catch if
        #the user clicks the upper corner, 'X' on windows OS
        self.master.protocol("WM_DELETE_WINDOW",lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets from a seperate module
        #keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)

        if __name__ == "__main__":
            root = tk.Tk()
            App = ParentWindow(root)
            root.mainloop()
