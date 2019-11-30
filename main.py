from buscador import *

if __name__=="__main__":
    usar=True
    buscar=Buscador()
    while usar:
        print("Bienvenidos al Sistema de Información \n Elija una opción:\n a) Buscar Curso por Código\n b)Buscar alumno por código\n c)Salir")
        buscar.conectar()
        eleccion=input()
        if eleccion=="c":
            print("Saliendo del sistema")
            usar=False
        elif eleccion=="a":
            codigo=input("Ingrese el código del curso")
            resultados=buscar.buscar_curso(codigo)
            for resultado in resultados:
                print("curso:"+ resultado[0]+" código: "+resultado[1]+" créditos: "+str(resultado[2]))

        elif eleccion=="b":
            print("Haz elegido la b")
        else:
            print("Haz elegido una opción no válida, vuelva a intentarlo")