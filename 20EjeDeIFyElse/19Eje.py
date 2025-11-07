

hora = int(input("Ingrese la hora: "))


if 0 <= hora <= 23:
    
    if 6 <= hora <= 11:
        turno = "Mañana"
    elif 12 <= hora <= 17:
        turno = "Tarde"
    elif 18 <= hora <= 23:
        turno = "Noche"
    else: 
        turno = "Madrugada"
    print(f"El turno es: {turno}")

else:
    print("Hora inválida. Debe ser un número entre 0 y 23.")
