calificaciones = []


for i in range(5):
    calificacionesPorEstudiante = []
    for j in range(5):
        calificacion = float(input(f"Digite la nota {j + 1} del estudiante {i + 1}: "))
        calificacionesPorEstudiante.append(calificacion)
   
    calificaciones.append(calificacionesPorEstudiante)
   
aprobados = 0


for i in range(len(calificaciones)):
    promedio = sum(calificaciones[i]) / len(calificaciones[i])
    print(f"Las calificaciones del estudiante {i + 1} son: {calificaciones[i]}")
    print(f"El promedio del estudiante {i + 1} es: {promedio}")
   
    if promedio >= 3.5:
        aprobados += 1
   
   
print(f"El total de estudiantes aprobados es de:  {aprobados}")