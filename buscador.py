import sqlite3

class Buscador:
    def __init__(self):
        self.cursor=None

    def conectar(self):
        conexion=sqlite3.connect("orce.db")
        self.cursor=conexion.cursor()
    def buscar_alumno(self,codigo):
        pass

    def buscar_curso(self, codigo):

        self.cursor.execute("select * from cursos where codigo=?",[codigo.upper()])
        resultados=self.cursor.fetchall()
        return resultados