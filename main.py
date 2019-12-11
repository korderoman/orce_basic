from buscador import *
from redactor import *

if __name__ == "__main__":
    usar=True
    buscador=Buscador()
    redactor=Redactor()
    while usar:
        print("Bienvenidos al Sistema de la Feria de Proyectos FIIS UNI 2019-B \n a)Ingresar Proyecto \n b) Jurado Evaluador \n c) Calificación de los Proyectos \n d)Resultados \n e) Salir" )
        opcion=input()
        if opcion=="e" or opcion=="E":
            print("Saliendo del sistema")
            usar=False
        elif opcion=="a" or opcion=="A":
            descripcion=buscador.listar_proyectos()
            redactor.redactar_proyectos_descripcion(descripcion)
        elif opcion=="b" or opcion=="B":
            jurados=buscador.listar_jurados()
            redactor.redactar_jurados(jurados)
        elif opcion=="c" or opcion=="C":
            calificaciones=buscador.listar_proyectos_calificados()
            redactor.redactar_proyectos_calificados(calificaciones)
        elif opcion=="d" or opcion=="D":
            print("indique el tipo de reporte que desea: \n 1-Por Categoría \n 2- 3 Primeros puestos por categoría \n 3-Proyectos por jurado Evaluador")
            submenu=input()
            if submenu=="1":
                a,b,c=buscador.listar_x_categorias()
                redactor.redactar_x_categoria(a,b,c)
            elif submenu=="2":
                a,b,c=buscador.listar_primeros()
                redactor.redactar_primeros_puestos(a,b,c)
            elif submenu=="3":
                jueces=buscador.buscar_x_jurado()
                redactor.redactar_proyecto_x_jurado(jueces)

            else:
                print("Ha elegido una opción equivocada, volviendo al menú principal")
            #obtenemos todos los proyectos por categoria
            
