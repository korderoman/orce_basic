class Controlador:

    def __init__(self, cursos_parametro):
        self.cursos=cursos_parametro

    def evaluar_menor_ciclo(self,opcion,matricula):
        menor=self.aux_valor_menor(matricula)
        if menor>=self.cursos[int(opcion)][2]:
            return True
        else:
            return False
    def aux_valor_menor(self,matricula):
        ciclos=[]
        ciclo_menor=None
        for curso in self.cursos:
            ciclos.append(curso[2])
        ciclo_menor=min(ciclos)
        return ciclo_menor

    
        
