
salario = float(input(" inserte su salario"))
descuento =0
exedente18mil= (30000 - 10000) * 0.1

if salario <= 10000:
    print(" no tienes impuesto para pagar")

elif salario<= 30000:
    descuento= (salario - 10000 ) *0.10
    print(f"tu salario es {salario} y tu descuento es {descuento}")

else:
    descuento= (salario - 30000) *0.20 + exedente18mil
    print(f" tu salario es {salario} y tu descuento es {descuento}")