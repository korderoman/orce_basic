#instala esta librería en la línea de comandos pip install PTable
from prettytable import PrettyTable
class Redactor:
    def __init__(self):
        self.tabla_cursos_disponibles=PrettyTable(["Opción","Código de Curso","Ciclo","Nota","Condición"])
        self.tabla_notas=PrettyTable(["Curso","Nota","Condición"])
        self.tabla_matricula=PrettyTable(["Curso","Créditos"])
    def redactar_alumno(self,alumnos):
        for alumno in alumnos:
            print("Alumno: "+alumno[2]+" "+alumno[3]+" "+alumno[0]+" "+alumno[1]+"\n Código: "+alumno[4]+"\n Especialidad: "+alumno[5]+"\n")
    
    def redactar_notas(self,notas):
        for nota in notas:
            self.tabla_notas.add_row([nota[1],str(nota[3]),nota[4]])
        print(self.tabla_notas)

    def redactar_cursos_disponibles(self,cursos):
        print("Cursos Disponibles")
        for i in range(len(cursos)):
            self.tabla_cursos_disponibles.add_row([ str(i),cursos[i][1],str(cursos[i][2]),str(cursos[i][3]),cursos[i][4]])
        print(self.tabla_cursos_disponibles)
    
    def redactar_matricula(self,matricula):
        print("Su ficha de Matrícula es:")
        for curso in matricula:
            self.tabla_matricula.add_row([curso[1],curso[3]])
        print(self.tabla_matricula)
