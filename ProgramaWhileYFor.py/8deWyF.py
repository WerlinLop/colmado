numero=int(input("ingrese un numero"))

if numero==1:
    print("0")
elif numero==2:
    print("0,1")
else:
    a, b, =0, 1
    print(a, end=", ")
    print(b, end=", ")

for i in range(2, numero):
    c= a + b
    print(c, end=", "if i < numero - 1 else "")
    a, b = b, c