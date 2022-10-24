

import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)#Doesn't allow for resize
        self.master.geometry('{}x{}'.format(700, 400))#This is the height and the width
        self.master.title('Learning Tkinter!')#This is the title
        self.master.config(bg='lightgray')#This is the overall background color
        
        self.varFname = StringVar()
        self.varLname = StringVar()

        #First name label
        self.lblFname = Label(self.master,text='First Name: ', font= ("Helvitica", 16), fg='black', bg='lightgray')
        self.lblFname.grid(row=0,column=0, padx=(30,0),pady=(30,0))

        #Last name label
        self.lblLname = Label(self.master,text='Last Name: ', font= ("Helvitica", 16), fg='black', bg='lightgray')
        self.lblLname.grid(row=1,column=0, padx=(30,0),pady=(30,0))


        #Label display
        self.lblDisplay = Label(self.master,text='', font= ("Helvitica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3,column=1, padx=(30,0),pady=(30,0))
        
        #First name text box
        self.txtFname = Entry(self.master,text=self.varFname, font= ("Helvitica", 16), fg='black', bg='lightblue')
        self.txtFname.grid(row=0,column=1, padx=(30,0),pady=(30,0))

        #Last name text box
        self.txtLname = Entry(self.master,text=self.varLname, font= ("Helvitica", 16), fg='black', bg='lightblue')
        self.txtLname.grid(row=1,column=1, padx=(30,0),pady=(30,0))

        #Submit button
        self.btnSubmit = Button(self.master, text="Submit", width=10, height = 2, command=self.submit)
        self.btnSubmit.grid(row=2,column=1, padx=(0,0),pady=(30,0), sticky=NE)

        #Cancel button
        self.btnCancel = Button(self.master, text="Cancel", width=10, height = 2, command=self.cancel)
        self.btnCancel.grid(row=2,column=1, padx=(0,100),pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFname.get()
        ln = self.varLname.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))


    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
