

print("="*50)
print("               *Bienvendo a Clases*")
print("="*50)
print("            Estas son tus Asignaturas ")
print("="*50)
asignatura=( "Matematica\nFisica\nQuimica\nHistoria\nLengua ")
print(asignatura)

mate=1
fis=1
qui=1
his=1
lengu=1

mate=int(input("\nInserte su Calificacion de Matematica: "))
fis=int(input("Inserte su Calificacion Fisica: "))
qui=int(input("Inserte su Calificacion Quimica: "))
his=int(input("Inserte su Calificacion Historia: "))
lengu=int(input("Inserte su Calificacion Lengua: "))


if 0<= mate and fis and qui and his and lengu <= 100:
     if 0<= mate <=100:
           print(f"\nMatematica: {mate}")
     else:
           print(f"Esta calificaciom {mate} no esta en el rango")
     if 0<=fis <=100:
           print(f"Fisica: {fis}")
     else:
           print(f"Esta calificacion {fis} no esta en el rango")
     if 0<= qui <=100:
           print(f"Quimica: {qui}")
     else:
           print(f"Esta calificacion {qui} no esta en el rango")
     if 0<= his<=100:
           print(f"Historia: {his}")
     else:
           print(f"Esta calificacion {his} no esta en el rango")
     if 0<= lengu <=100:
           print(f"Lengua: {lengu}")
     else:
           print(f"Esta calificacion {lengu} no esta en el rango")



