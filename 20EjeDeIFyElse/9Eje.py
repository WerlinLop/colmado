numero1= int(input("Inserte su primer numero\n"))
numero2= int(input("Inserte su Segundo numero\n"))
numero3= int(input("Inserte se Tercer numero\n"))

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} es mayor")

elif numero2 >numero1 and numero2 > numero3:
    print(f"{numero2} es mayor")

else:
    print(f"{numero3} es Mayor")