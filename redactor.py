#instala esta librería en la línea de comandos pip install PTable
from prettytable import PrettyTable
class Redactor:
    def __init__(self):
        self.tabla_proyectos_descripcion=PrettyTable(["Nombre del Proyecto","Curso","Ciclo","Integrante 1","Integrante 2", "Integrante 3"])
        self.tabla_jurados=PrettyTable(["Nombre","Especialidad","Código"])
        self.tabla_calificaciones=PrettyTable(["Nombre","J1-Proyecto","J1-Exposición","J1-Ambiental","J1-Paper","J1-Promedio","J2-Proyecto","J2-Exposición","J2-Ambiental","J2-Paper","J2-Promedio"])
        self.tabla_A=PrettyTable()
        self.tabla_B=PrettyTable()
        self.tabla_C=PrettyTable()
        self.tabla_primeros_A=PrettyTable(["Nombre","Total"])
        self.tabla_primeros_B=PrettyTable(["Nombre","Total"])
        self.tabla_primeros_C=PrettyTable(["Nombre","Total"])
        self.tabla_proyecto_juez=PrettyTable(["Juez","Proyecto"])
        #a partir de aqui
    def redactar_proyectos_descripcion(self,descripcion):
        for proyecto in descripcion:
            self.tabla_proyectos_descripcion.add_row([proyecto[0],proyecto[1],proyecto[2],proyecto[3],proyecto[4],proyecto[5]])
        print(self.tabla_proyectos_descripcion)
    
    def redactar_jurados(self,jurados):
        for jurado in jurados:
            self.tabla_jurados.add_row([jurado[0],jurado[1],jurado[2]])
        print(self.tabla_jurados)
    
    def redactar_proyectos_calificados(self,calificaciones):
        for proyecto in calificaciones:
            self.tabla_calificaciones.add_row([proyecto[0],proyecto[1],proyecto[2],proyecto[3],proyecto[4],proyecto[5],proyecto[6],proyecto[7],proyecto[8],proyecto[9],proyecto[10]])
        print(self.tabla_calificaciones)

    def redactar_x_categoria(self,a,b,c):
        self.tabla_A.add_column("Categoria A",a)
        self.tabla_B.add_column("Categoria B",b)
        self.tabla_C.add_column("Categoria C",c)
        print(self.tabla_A)
        print(self.tabla_B)
        print(self.tabla_C)
    
    def redactar_primeros_puestos(self,a,b,c):
        arreglos=[a,b,c]
        tablas=[self.tabla_primeros_A,self.tabla_primeros_B,self.tabla_primeros_C]
        titulos=["Categoría A","Categoría B","Categoría C"]
        for i in range(len(arreglos)):
            for proyecto in arreglos[i]:
                tablas[i].add_row([proyecto[0],float(proyecto[23])])
                #print(proyecto[0],proyecto[23])
            tablas[i].sortby="Total" #ordenamos
            tablas[i].reversesort=True #invertimos el orden
            print(tablas[i].get_string(start=0, end=3,title=titulos[i]))

    def redactar_proyecto_x_jurado(self,jueces):
        for juez in jueces:
            self.tabla_proyecto_juez.add_row([juez[1],juez[0]])
        self.tabla_proyecto_juez.sortby="Juez"
        print(self.tabla_proyecto_juez)
        