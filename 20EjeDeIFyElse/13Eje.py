print("----Bienvenido----")
año= int(input("Inserte un año\n"))

if (año % 4 ==0 and año % 100 !=0 ) or (año% 400==0):
    print(f"el año{año} es bisiesto")

else:
    print(f"el año{año} no es bisisto")