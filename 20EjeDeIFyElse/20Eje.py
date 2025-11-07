
print("---Bienvenido a la Maquina de Peso---")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))


Imc = peso / (altura ** 2)


if Imc < 18.5:
    categoria = "Bajo peso"

elif 18.5 <= Imc <= 24.9:
    categoria = "Normal"

elif 25 <= Imc <= 29.9:
    categoria = "Sobrepeso"

else:  
    categoria = "Obesidad"



print(f"Su IMC es: {Imc:.2f}")

print(f"Categoría: {categoria}")
