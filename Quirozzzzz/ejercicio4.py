Hora_trabajadas= 48
Pago_por_hora= 6471
Pago_hora_Extra= 8088
# Calcular el pago total por horas trabajadas
Pago_total = (Hora_trabajadas* 4) * Pago_por_hora
print("El pago mensual es:", Pago_total)


print("----------------------------------")


if Pago_total > 2847000:
    print("Tiene derecho a auxilio de transporte")
else:
    print("No tiene derecho a auxilio de transporte")


print("----------------------------------")


Horas_Extras= int(input("Ingrese las horas extras trabajadas diurnas: "))
TotalPago_Horas_Extras= Horas_Extras * Pago_hora_Extra
print("El pago por horas extras es:", TotalPago_Horas_Extras)
Pago_total_h = (Hora_trabajadas* 4) * Pago_por_hora + TotalPago_Horas_Extras
print("El nuevo pago total con horas extras es:", Pago_total_h)


print("----------------------------------")
print("Deducciones aplicadas")
Deduccion_EMI= Pago_total_h * 0.03  # Deducción para EMI
Deduccion_Funeraria= Pago_total_h * 0.02  # Deducción de funeraria
Salario_con_deducciones= Pago_total_h - Deduccion_EMI - Deduccion_Funeraria
print("Deducción EMI:", Deduccion_EMI)
print("Deducción Funeraria:", Deduccion_Funeraria)
print("El salario bruto después de deducciones es:", Salario_con_deducciones)


print("----------------------------------")


Aporte= input("¿Realiza aporte para  el fondo de empleados? (si/no): ")
if Aporte.lower() == "si":
    Valor_aporte= float(input("Ingrese el valor a aportar: "))
    Salario_Neto= Salario_con_deducciones - Valor_aporte
    print("El salario neto después de aportes a empleados es:", Salario_Neto)
elif Aporte.lower() == "no":
    print("El salario con las deducciones es:", Salario_con_deducciones)
else:
    print("El valor ingresado no es correcto.")


print("----------------------------------")


if Pago_total_h > 3740000:
    Dedudccion_alimentos= Salario_Neto * 0.30 + Salario_Neto
    print("El salario neto después de la demanda de alimentos es:", Dedudccion_alimentos)
else:
    print("Termino el programa sin deducciones adicionales.")


print("Horas trabajadas:", Hora_trabajadas)
print("Horas extras trabajadas:", Horas_Extras)
print("Deducción EMI:", Deduccion_EMI)
print("Deducción Funeraria:", Deduccion_Funeraria)
if Aporte.lower() == "si":
    print("Deducción empleados:", Valor_aporte)
elif Aporte.lower() == "no":
    print("Deducción empleados: 0")
print("El salario Bruto es:", Pago_total_h)
if Aporte.lower() == "si":
    Valor_aporte= float(input("Ingrese el valor a aportar: "))
    Salario_Neto= Salario_con_deducciones - Valor_aporte
    print("El salario neto después de aportes a empleados es:", Salario_Neto)
    print("El salario Neto es:", Salario_Neto )
else: print("El salario Neto es:", Salario_con_deducciones )