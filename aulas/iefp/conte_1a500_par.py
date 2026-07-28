numero = 1
while  numero <10:
    p = numero % 2
    if p  == 1 : # == serve para compara os dois valores sao iguais
        print(f"{numero} é impar", end=" ")
    
    else:
        print(f"{numero} par", end= " ")
    
    numero += 1     
   

