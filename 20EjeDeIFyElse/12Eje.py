
numero1= int(input(" inserte su Primer numero")) 
numero2=int(input(" inserte su Segundo numero")) 
numero3=int(input(" inserte su Tercer numero")) 

if numero1==0 or numero2== 0 or numero3==0:
    print(f"{numero1}\n{numero2}\n{numero3}\n uno de estos numero hay cero")

elif numero1> 0 and numero2>0 and numero3>0:
    print(f"{numero1}\n{numero2}\n{numero3}\n ---Son positivos---")

elif numero1 <0 and numero2<0 and numero3<0: 
    print (f"{numero1}\n{numero2}\n{numero3}\n ---Son Negativo---")
   
else:
    print("los numeros son mixtos")

