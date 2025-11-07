
numero=int(input("Inserte un numero\n"))

factorial=1
resultado=1

while resultado<= numero:
    factorial*= resultado
    resultado += 1

print(f"el Factorial  {numero}\nEs {factorial}")
