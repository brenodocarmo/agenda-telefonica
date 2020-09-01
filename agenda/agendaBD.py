import sqlite3


class UsuarioBD:

    def conectaBD(self):
        """
            Cria o Banco de Dados, e cria um objeto para manipular as instruções SQL
        """
        self.conn = sqlite3.connect("agenda.db")
        self.cursor = self.conn.cursor()
        print("Conectado ao Banco de Dados")

    def desconctaBD(self):
        """Fecha a conexão com o Banco de Dados"""
        self.conn.close()
        print("Desconectado do Banco de Dados")

    def create_table(self):
        """Criar uma tabela caso ela não exista"""
        self.conectaBD()
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS contato(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome CHAR(50) NOT NULL,
                    numero VARCHAR NOT NULL,
                    email CHAR(40) NOT NULL
                ); 
            """
            )
        except Exception as ex:
            print(f"Ocorreu um erro na criação do BD: {ex}")
        else:
            self.conn.commit()
            self.desconctaBD()
            print("Criado com sucesso!!!!")

    def insert_contact(self, usuario):
        """
            Inseri os registro no banco de Dados.
            :param nome
            :param numero
            :param email
        """
        self.conectaBD()
        try:
            self.cursor.execute(
                """
                INSERT INTO contato(nome, numero, email)
                VALUES(?, ?, ?)
            """,
                usuario,
            )
        except Exception as ex:
            print(f"Não foi possivel realizar essa operação, ERRO: {ex}")

            # Desfaz as operações realizada
            self.conn.rollback()
        else:
            self.conn.commit()
            self.desconctaBD()
            print("Dados inseridos com sucesso!!!")

    def find_contact(self):
        self.conectaBD()
        try:
            var = self.cursor.execute("""
                SELECT * FROM contato

            """)
        except Exception as ex:
            print(f"ERRO: {ex}")
            self.conn.rollback()
        else:
            return var.fetchall()

    def show_contact(self):
        self.conectaBD()
        lista = self.find_contact()
        for i, nome, tel, ema in lista:
            print(i, nome, tel, ema)

    def update_contact(self, nome, numero, email, rowd):
        """
            Atualizar(modificar) os registro existentes
            :param nome
            :param numero
            :param email
        """
        self.conectaBD()
        try:
            self.cursor.execute(
                """
                UPDATE contato SET nome=?, numero=?, email=?
                WHERE id=?
            """,
                (nome, numero, email, rowd),
            )

        except Exception as ex:
            print(f"Não foi possivel realiazar essa operação, ERRO: {ex}")
            self.conn.rollback()
        else:
            self.conn.commit()
            self.desconctaBD()
            print("Contato modificado com sucesso!!!")

    def delete_contact(self, rowd):
        """
            Excluir o contato que foi inserido na tabela passando apenas o id
            :param id
        """
        self.conectaBD()
        try:
            self.cursor.execute(
                """
                DELETE FROM contato WHERE id=?
            """,
                (rowd,),
            )

        except Exception as ex:
            print(f"Não foi possivel realizar essa operação, ERRO: {ex}")
            self.conn.rollback()
        else:
            self.conn.commit()
            self.desconctaBD()
            print("Contato apagado com sucesso!!!")
