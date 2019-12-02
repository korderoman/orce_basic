from buscador import *
from redactor import *
from controlador import *

if __name__=="__main__":
    usar=True
    buscar=Buscador()
    redactor=Redactor()    
    while usar:
        print("Bienvenidos al Sistema de Matrícula \n Ingrese su código de estudiante\n Salir del Sistema - presione la tecla x \n")
        codigo=input()
        if(codigo=="x"):
            print("Saliendo del Sistema de Matrícula")
            usar=False
        else:
            alumno=buscar.buscar_alumno(codigo)
            if alumno:
                redactor.redactar_alumno(alumno)
                usar2=True
                while usar2:
                    print("Tiene las siguientes opciones")
                    print("A) Notas  \n B) Matrícula \n C) Salir de las opciones")
                    opcion=input()
                    if opcion=="c" or opcion=="C":
                        print("Saliendo de las opciones")
                        usar2=False
                    elif opcion=="a" or opcion=="A":
                        notas=buscar.buscar_notas(codigo)
                        redactor.redactar_notas(notas)
                    elif opcion=="b" or opcion=="B":
                        matriculado=buscar.get_matriculado(codigo)
                        if matriculado[0][0]=="NO":                        
                            matricula=[] # se crea una lista que almacenará la matricula
                            cursos=buscar.buscar_cursos_disponible(codigo)
                            redactor.redactar_cursos_disponibles(cursos)
                            usar3=True
                            controlador=Controlador(cursos)
                            while usar3:
                                opcion=input("Indique el curso que desea matricularse en función de la opción o presione z si desea finalizar la matricula ")
                                if opcion=="z":
                                    usar3=False
                                    #imprimimos la matricula
                                    redactor.redactar_matricula(matricula)
                                    buscar.set_matriculado(codigo)
                                else:
                                    opcion=int(opcion)
                                    if opcion<len(cursos):
                                        matricular=controlador.evaluar_menor_ciclo(opcion,matricula)
                                        if matricular:
                                            if cursos[opcion] in matricula:
                                                print("ya está matriculado")
                                            else:
                                                print("Matriculando")
                                                matricula.append(cursos[opcion])
                                        else:
                                            print("Debe elegir primero un curso de menor ciclo")
                                    else:
                                        print("No ha elegido una opción válida")
                        else:
                                print("Usted ya se encuentra matriculado")
                    else:
                        print("Opción incorrecta")
            else:
                print("Alumno no encontrado, escriba un código correcto")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        print("Bienvenidos al Sistema de Información \n Elija una opción:\n a) Notas\n b)Matrícula\n c)Salir")
        
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
        """