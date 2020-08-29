from tkinter import *
from tkinter import ttk


root = Tk()

class Agenda:

    def __init__(self):
        self.root = root
        self.tela()
        self.frame_tela()
        self.widgts_frame_1()
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

    # Criação dos Butões
    def widgts_frame_1(self):
        
        #Criação do botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=2, bg="#dcdcdc", 
                                fg="#000000", font=("verdana", 10, "bold"))
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        #Criação do botão Buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg="#dcdcdc", 
                                fg="#000000", font=("verdana", 10, "bold"))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        #Criação do botão Novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg="#dcdcdc", fg="#000000",
                            font=("verdana", 10, "bold"))
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        #Criação do botão Alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=2, bg="#dcdcdc",
                                fg="#000000", font=("verdana", 10,"bold"))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        #Criação do botão Apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd=2, bg="#dcdcdc",
                                fg="#000000", font=("verdana", 10, "bold"))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)


        # Criação da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text="Código", bg="#fff5ee",
                                font=("verdana", 10))
        self.lb_codigo.place(relx=0.05, rely=0.05)
        # Criação da Entry do código
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        # Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text="Nome", bg="#fff5ee",font=("verdana", 10))
        self.lb_nome.place(relx=0.045, rely=0.35, relwidth=0.08)
        # Criação da Entry do nome
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)


        # Criação da label e entrada do telefone
        self.lb_fone = Label(self.frame_1, text="Telefone", bg="#fff5ee", 
                            font=("verdana", 10))
        self.lb_fone.place(relx=0.05, rely=0.6)
        # Criação da Entry do telefone
        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        # Criação da label e entrada da cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade", bg="#fff5ee", 
                                font=("verdana", 10))
        self.lb_cidade.place(relx=0.5, rely=0.6)
        # Criação da Entry do telefone
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

Agenda()
