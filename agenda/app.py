from tkinter import *
from tkinter import ttk


root = Tk()

class Agenda:

    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    
    def tela(self):
        self.root.title("Agenda Telefônica")
        self.root.configure(bg="#ADD8E6")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=700)
        self.root.minsize(width=500, height=400)

Agenda()