

lado1 = float(input("Ingrese la primera longitud\n "))
lado2 = float(input("Ingrese la segunda longitud\n "))
lado3 = float(input("Ingrese la tercera longitud\n "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        tipo = "equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "isósceles"
    else:
        tipo = "escaleno"
    print(f"Los lados forman un triángulo {tipo}.")
else:
    print("Los lados no pueden formar un triángulo.")
