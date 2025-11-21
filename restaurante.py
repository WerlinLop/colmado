
#Crea un programa que muestre un menú para un restaurante con 10 productos.
#El programa debe capturar cada venta en una lista y al final mostrar las ventas por tipo de 
#producto y el total de las ventas



menu = [
    ("Hamburguesa", 80),
    ("Hot Dog", 50),
    ("Pizza", 120),
    ("Tacos", 15),
    ("Refresco", 20),
    ("Café", 25),
    ("Papas fritas", 30),
    ("Ensalada", 60),
    ("Sándwich", 70),
    ("Postre", 45)
]

ventas = []

def restaurante():
    for i, (producto, precio) in enumerate(menu):
        print(f"{i+1}. {producto} - {precio}")
    print ("0 para concluir")


while True:
    restaurante()
    plato = input("Ingrese el número del producto vendido (0 para terminar): ")

    if not plato.isdigit():
        print(" Entrada no válida. Intente de nuevo.")
        continue

    plato = int(plato)

    if plato == 0:
        break
    elif 1 <= plato <= 10:
        ventas.append(plato - 1)
        print("✔ Venta registrada.")
    else:
        print(" Opción fuera del rango.")

conteo=[0]* len(menu)
total= 0

for x in ventas:
    conteo [x] += 1
    total += menu[x] [1]

print("Reporte de ventas")
for i, (producto, precio) in enumerate(menu):
    print(f"{producto}: {conteo[i]} ventas - ${conteo[i] * precio}")

print(f"\n El total de ventas{total}")