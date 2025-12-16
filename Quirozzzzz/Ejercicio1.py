#Ingreso de notas
Nota1= float(input("Ingrese la primera nota 1: "))
Nota2= float(input("Ingrese la primera nota 2: "))
Nota3= float(input("Ingrese la primera nota 3: "))
Nota4= float(input("Ingrese la primera nota 4: "))
#Promedio de las notas
Promedio= (Nota1 + Nota2 + Nota3 + Nota4) / 4
print("El promedio de las notas es: ", Promedio)
#Evaluacion del promedio obtenido
if Promedio==0.0 or Promedio>5.0:
    print("La nota ingresada no es valida.")
elif Promedio <3.4:
    print ("El estudiante Reprobó la asignatura, debe reforzar sus conocimientos para el proximo periodo.")
elif Promedio>=3.5 and Promedio<=3.9:
    print ("El estudiante Aprobó la asignatura, pero debe reforzar.")
elif Promedio>=4.0 and Promedio<=4.5:
    print ("El estudiante Aprobó la asignatura con sobresaliencia.")
elif Promedio>=4.6 and Promedio<=5.0:
    print ("El estudiante Aprobó, obtiene un nivel de excelencia y se le cita a comite para felicitarlo.")
#Reconocimientos adicionales si abrobo
if Promedio >=3.5:
    Comportamiento= input("Ingrese el comportamiento del estudiante (Excelente, Bueno): ")
    if Comportamiento=="Excelente":
        print ("Felicitaciones por su exelente desempeño academico y por ser un ejemplo a seguir.")
    elif Comportamiento=="Bueno":
        print ("Buen trabajo, siga asi para mejorar aun mas.")
    else:
        print ("Sin recomendación adicional.")
else:
    print ("Sin recomendación adicional.")
