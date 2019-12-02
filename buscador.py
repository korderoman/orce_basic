import sqlite3

class Buscador:
    def __init__(self):
        self.cursor=None
        self.conexion=None
    def conectar_consultar(self,consulta,variable):
        self.conexion=sqlite3.connect("orce2.db")
        self.cursor=self.conexion.cursor()
        self.cursor.execute(consulta,[variable])
        resultados=self.cursor.fetchall()
        self.conexion.commit()
        self.conexion.close()
        return resultados
        
    def buscar_alumno(self,codigo):
        consulta="select * from alumnos where CODIGO=?"
        variable=codigo.upper()
        return self.conectar_consultar(consulta,variable)
    
    def buscar_notas(self,codigo):
        consulta="select * from NOTAS where CODIGO=? and not CONDICION='NO LLEVADO'"
        variable=codigo.upper()
        return self.conectar_consultar(consulta,variable)

    def buscar_curso(self, codigo):
        consulta="select * from cursos where codigo=?"
        variable=codigo.upper()
        return self.conectar_consultar(consulta,variable)

    def buscar_cursos_disponible(self,codigo):
        consulta="select * from NOTAS where CODIGO=? and (CONDICION='NO LLEVADO' or CONDICION='DESAPROBADO')"
        variable=codigo.upper()
        return self.conectar_consultar(consulta,variable)
    
    def get_matriculado(self,codigo):
        consulta="select MATRICULADO from alumnos where CODIGO=?"
        variable=codigo.upper()
        return self.conectar_consultar(consulta,variable)

    def set_matriculado(self,codigo):
        consulta="update alumnos set MATRICULADO='SI' where CODIGO=?"
        variable=codigo.upper()
        self.conectar_consultar(consulta,variable)