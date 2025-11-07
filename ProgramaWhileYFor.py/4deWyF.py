
print("Calcula la suma de los numeros del 1, al 100")

resultado=0

for numero in range (1,101):
    producto=resultado
    resultado +=numero 
    print(f"sumando{numero}: {producto} + {numero} = {resultado}")

print(f"la suma total de los numeros de 1 al 100 es {resultado}")