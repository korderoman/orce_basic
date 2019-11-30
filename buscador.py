import sqlite3

class Buscador:
    def __init__(self):
        self.cursor=None

    def conectar(self):
        conexion=sqlite3.connect("orce.db")
        self.cursor=conexion.cursor()
    def buscar_alumno(self,codigo):
        self.cursor.execute("select * from notas_industriales where codigo=?",[codigo.upper()])
        resultados1=self.cursor.fetchall()
        self.cursor.execute("select * from alumnos where codigo=?",[codigo.upper()])
        resultados2=self.cursor.fetchall()
        self.cursor.execute("select * from notas_sistemas where codigo=?",[codigo.upper()])
        resultados3=self.cursor.fetchall()
        return resultados1, resultados2,resultados3

    def buscar_curso(self, codigo):
        self.cursor.execute("select * from cursos where codigo=?",[codigo.upper()])
        resultados=self.cursor.fetchall()
        return resultados