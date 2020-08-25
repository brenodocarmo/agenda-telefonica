from tkinter import *
from tkinter import ttk


root = Tk()

class Agenda:

    def __init__(self):
        self.root = root
        self.tela()
        self.frame_tela()
        root.mainloop()

    def tela(self):
        self.root.title("Agenda Telefônica")
        self.root.configure(bg="#dcdcdc")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=800, height=700)
        self.root.minsize(width=500, height=400)

    def frame_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg="#fff5ee", highlightbackground="#fff5ee", 
                            highlightthickness=1)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.45)

        self.frame_2 = Frame(self.root, bd=4, bg="#fff5ee", highlightbackground="#fff5ee",
                             highlightthickness=1)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.45)


Agenda()