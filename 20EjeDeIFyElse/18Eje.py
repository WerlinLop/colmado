
print( "---bienvenido---")
temperatura = float(input("Ingrese la temperatura en °C: "))

if temperatura < 0:
    print("Hace mucho frío")

elif 0 <= temperatura <= 20:
    print("Clima fresco")

elif 21 <= temperatura <= 30:
    print("Clima agradable")

else:  
    print("Hace mucho calor")
