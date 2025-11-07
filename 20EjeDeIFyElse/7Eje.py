
print("Bienvenido al Calendario")

semana= int(input("Ingrese un número del 1 al 7 "))


if 1 <= semana <= 7:
    
    if semana== 1:
        dia = "Lunes"
    
    elif semana == 2:
        dia = "Martes"
    
    elif semana == 3:
        dia = "Miércoles"
    
    elif semana == 4:
        dia = "Jueves"
    
    elif semana == 5:
        dia = "Viernes"
    
    elif semana == 6:
        dia = "Sábado"
    
    else: 
        dia = "Domingo"
    print(f"El día de la semana es {dia}")
else:
    print("Número inválido Debe ser un número entre 1 y 7")
