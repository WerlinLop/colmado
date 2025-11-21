# Menú de productos (nombre, precio)
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

ventas = []  # Aquí se guardan las ventas (índices de productos)

def mostrar_menu():
    print("\n===== MENÚ DEL RESTAURANTE =====") 
    for i, (producto, precio) in enumerate(menu):
        print(f"{i+1}. {producto} - ${precio}")
    print("0. Terminar ventas")
    print("================================")

# Captura de ventas
while True:
    mostrar_menu()
    opcion = input("Ingrese el número del producto vendido (0 para terminar): ")

    # Validar entrada
    if not opcion.isdigit():
        print("❌ Entrada no válida. Intente de nuevo.")
        continue

    opcion = int(opcion)

    if opcion == 0:
        break
    elif 1 <= opcion <= 10:
        ventas.append(opcion - 1)
        print("✔ Venta registrada.")
    else:
        print("❌ Opción fuera del rango.")

# Cálculo de ventas
conteo = [0] * len(menu)
total = 0

for v in ventas:
    conteo[v] += 1
    total += menu[v][1]

# Reporte final
print("\n===== REPORTE DE VENTAS =====")
for i, (producto, precio) in enumerate(menu):
    print(f"{producto}: {conteo[i]} ventas - ${conteo[i] * precio}")

print("\nTOTAL DE VENTAS: $", total)
print("=============================")
