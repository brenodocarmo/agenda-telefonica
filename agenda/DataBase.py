import sqlite3
import tkinter as tk


class AgendaDB:

    def conect_db(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")

    def desconectar_bd(self):
        self.conn.close(); print("Desconectando banco de dados")

    def montaTabelas(self):
        self.conect_db(); 
        # Criar Tabelas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente(
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(50) NOT NULL,
                telefone INTEGER(20)NOT NULL,
                email CHAR(40) NOT NULL
            );
        """)
        self.conn.commit(); print("Banco e Dados criado")
        self.desconectar_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.email = self.email_entry.get()

    def add_cliente(self):
        self.variaveis()
        self.conect_db()

        self.cursor.execute("""
            INSERT INTO cliente(nome_cliente, telefone, email)
            VALUES(?,?,?)""", (self.nome, self.fone, self.email))

        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.clear_display()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conect_db()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, email FROM cliente ORDER BY nome_cliente;""")
        for i in lista:
            self.listaCli.insert("", tk.END, values=i)
        self.desconectar_bd()


    def deleta_cliente(self):
        self.variaveis()
        self.conect_db()
        self.cursor.execute("""
            DELETE FROM cliente WHERE cod=?
        """,(self.codigo))
        self.conn.commit()
        self.clear_display()
        self.select_lista()

    def altera_cliente(self):
        self.variaveis()
        self.conect_db()
        self.cursor.execute("""
            UPDATE cliente SET nome_cliente=?, telefone=?, email=?
            WHERE cod=?
        """,(self.nome, self.fone, self.email, self.codigo))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.clear_display()

    def busca_cliente(self):
        self.conect_db()
        self.listaCli.delete(*self.listaCli.get_children())
        self.nome_entry.insert(tk.END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute("""
            SELECT cod, nome_cliente, telefone, email FROM cliente
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC
        """% nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", tk.END, values=i)
        self.clear_display()
        self.desconectar_bd()