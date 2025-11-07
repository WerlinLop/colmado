
producto= float(input("Inserte en precio del producto\n"))
descuneto=0

if producto<50:
    descuento=0

elif 51<producto<100:
    descuento =0.05

else:
    descuento=0.10

preciofinal= producto*(1 - descuento)

print(f"Descuento aplicado: {descuento*100:.0f}%")
print(f"Precio final: ${preciofinal:.2f}")
