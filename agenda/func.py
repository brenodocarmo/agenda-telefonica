
import tkinter as tk
from DataBase import AgendaDB


class Clear(AgendaDB):

    def clear_display(self):
        self.codigo_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.fone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def onDoubleclick(self, event):
        self.clear_display()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, "values")
            self.codigo_entry.insert(tk.END, col1)
            self.nome_entry.insert(tk.END, col2)
            self.fone_entry.insert(tk.END, col3)
            self.email_entry.insert(tk.END, col4)

