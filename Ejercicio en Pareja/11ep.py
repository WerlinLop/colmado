
lista1=[1, 2, 3]
lista2=[-1, 0, 2]
producto= 0

for escalar in range(len(lista1)):
    producto += lista1[escalar] * lista2[escalar]

print(f"El producto a escalar es: {producto}")