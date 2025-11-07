
lado1=int(input("Inserte su Primer lado"))
lado2=int(input("Inserte su Segundo lado"))
lado3=int(input("Inserte su Tercer lado"))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("los lados pueden formar un triángulo")

else:
    print("los lados no pueden formar un triangulo")