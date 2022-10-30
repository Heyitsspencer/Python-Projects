import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    #Makes the window itself
    def __init__(self,master):
        Frame.__init__(self,master)
        self.columnconfigure(3, weight=1)
        #Title
        self.master.title("Web Page Generator")
        self.label1 = Label(text="Enter custom text or click the Default HTML page button")
        self.label1.grid(padx=(10,10), pady=(10,10),row=0, column=0)
        #Text box
        self.entry1 = Entry(width=100)
        self.entry1.grid(padx=(10,10), pady=(10,10), row=1, column=0, columnspan=3)
        
        #HTML Button ("Default HTML Page")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10), pady=(10,10),row=2, column=2)
        #Submit custom text button
        self.btn = Button(self.master, text="Submit custom text", width=30, height=2, command=self.customText)
        self.btn.grid(padx=(10,10), pady=(10,10),row=2, column=3)
    #Adds functionality to the HTML button
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
    def customText(self):
        htmlText = self.entry1.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        








if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
