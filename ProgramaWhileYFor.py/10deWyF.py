
contraseñaCorrecta= "Werlin123"

contraseñaIngresada=""

while True:
    contraseñaIngresada = input("Ingrese una contraseña\n")
    if contraseñaIngresada == contraseñaCorrecta:
        print("contrasseña correcta")
        break
         
    else:
        print("Contraseña Incorrecta")
