from buscador import *

if __name__=="__main__":
    usar=True
    buscar=Buscador()
    while usar:
        print()
        print()
        print("Bienvenidos al Sistema de Información \n Elija una opción:\n a) Buscar Curso por Código\n b)Buscar alumno por código\n c)Salir")
        buscar.conectar()
        eleccion=input()
        if eleccion=="c":
            print("Saliendo del sistema")
            usar=False
        elif eleccion=="a":
            codigo=input("Ingrese el código del curso")
            cursos=buscar.buscar_curso(codigo)
            for curso in cursos:
                print("curso:"+ curso[0]+" código: "+curso[1]+" créditos: "+str(curso[2]))
            
        elif eleccion=="b":
            codigo=input("Ingrese el código del alumno")
            notas_ind,alumnos,notas_sis=buscar.buscar_alumno(codigo)
            for alumno in alumnos:
                print("Alumno: "+alumno[2]+" "+alumno[3]+" "+alumno[0]+" "+alumno[1]+"\n Código: "+alumno[4]+"\n Especialidad: "+alumno[5]+"\n Cursos:")
                if alumno[5]=="industrial":
                    for nota in notas_ind:
                        print("Cálculo Diferencial: "+ str(nota[1]))
                        print("Química I: "+ str(nota[2]))
                        print("Redacción y Comunicación: "+ str(nota[3]))
                        print("Ética y Filosofía política: "+ str(nota[4]))
                        print("Geometría Analítica: "+ str(nota[5]))
                        print("Dibujo en Ingeniería: "+ str(nota[6]))
                        print("Introducción a la Ing. Industrial: "+ str(nota[7]))
                else:
                    for nota in notas_sis:
                        print("Geometría Analítica: "+ str(nota[1]))
                        print("Cálculo Diferencial: "+ str(nota[2]))
                        print("Química I: "+ str(nota[3]))
                        print("Introducción a la Computación: "+ str(nota[4]))
                        print("Redacción y Comunicación: "+ str(nota[5]))
                        print("Introducción al pensamiento y a la Ing Sistemas: "+ str(nota[6]))
                
            
        else:
            print("Haz elegido una opción no válida, vuelva a intentarlo")