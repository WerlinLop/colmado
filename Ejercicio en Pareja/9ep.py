print("inserte una palabra: ")
palabra= (input ())
lista=[palabra]
vocales= "aeiouAEIOU"
cantidad=  {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0 }

pala=palabra.lower()

for vocal in vocales:
    if vocal  in pala:
        cantidad [vocal] = pala.count(vocal)

for vocal, resultado in cantidad.items():
    print (f"la vocal {vocal} aparece {resultado} veces")