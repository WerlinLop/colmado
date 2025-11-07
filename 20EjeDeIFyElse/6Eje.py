
print("-----.Bienvenido Al Los Resultados.-----")

calificacion= int(input("Digite su Calificacion\n"))


if 0<= calificacion <= 100 :
    
    if calificacion>=60:
        print("Aprobaste")

    else:
        print("Reprobaste")

else:
    print("la calificacion esta fuera de rango")
    