
angulo= int(input("inserte un grado"))



if  0 <  angulo <90 :
    print(f"{angulo} es agudo")
    
elif 90 < angulo < 179:
    print(f"{angulo} es obtuso")
        
else :
    angulo == 180
    print(f"{angulo} es llano")