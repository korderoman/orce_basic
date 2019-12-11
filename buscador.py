import csv

class Buscador:
    def __init__(self):
        self.proyectos=[]
        self.iniciar()
        

    def iniciar(self):
        with open("p2.csv","r") as file:
            reader=csv.reader(file)
            for row in reader:
                aux=row[0].split(";")
                self.proyectos.append(aux)

    def listar_proyectos(self):
        #debe mostrar los datos del proyecto nombre, curso, ciclo e integrantes
        descripcion=[]
        for proyecto in self.proyectos:
            aux=[]
            for i in range(6):
                aux.append(proyecto[i])
            descripcion.append(aux)
        return descripcion
                
    def listar_jurados(self):
        jurados=[]
        for jurado in self.proyectos:
            aux=[]
            for i in range(7,10):
                aux.append(jurado[i])
            jurados.append(aux)
            aux=[]
            for i in range(10,13):
                aux.append(jurado[i])
            jurados.append(aux)
        #eliminamos los duplicados
        jurados_final=[]
        for jurado in jurados:
            if jurado not in jurados_final:
                jurados_final.append(jurado)
        return jurados_final

    def listar_proyectos_calificados(self):
        calificaciones=[]
        for proyecto in self.proyectos:
            aux=[]
            aux.append(proyecto[0])
            for i in range(13,24):
                aux.append(proyecto[i])
            calificaciones.append(aux)
        return calificaciones

    def listar_x_categorias(self):
        tipo_a=[]
        tipo_b=[]
        tipo_c=[]
        for proyecto in self.proyectos:
            if proyecto[6]=="A":
                tipo_a.append(proyecto[0])
            elif proyecto[6]=="B":
                tipo_b.append(proyecto[0])
            elif proyecto[6]=="C":
                tipo_c.append(proyecto[0])
        return tipo_a,tipo_b,tipo_c

    
    def listar_primeros(self):
        tipo_a=[]
        tipo_b=[]
        tipo_c=[]
        for proyecto in self.proyectos:
            if proyecto[6]=="A":
                tipo_a.append(proyecto)
            elif proyecto[6]=="B":
                tipo_b.append(proyecto)
            elif proyecto[6]=="C":
                tipo_c.append(proyecto)
        return tipo_a,tipo_b,tipo_c
    
    def buscar_x_jurado(self):
        jueces=[]
        for proyecto in self.proyectos:
            aux=[]
            aux.append(proyecto[0])
            aux.append(proyecto[7])
            jueces.append(aux)
        
        for proyecto in self.proyectos:
            aux=[]
            aux.append(proyecto[0])
            aux.append(proyecto[10])
            jueces.append(aux)
        return jueces