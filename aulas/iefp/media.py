n1 = ["5","9","7"]
n2 = ["3","9","6"]
n3 = ["10","8","9"]

soma1 = int(n1[0]) + int(n1[1]) + int(n1[2]) 
soma2 = int(n2[0]) + int(n2[2]) + int(n2[2]) 
soma3 = int(n3[0]) + int(n3[2]) + int(n3[2])  
resultado1 = int(soma1/3)
resultado2 = int(soma2/3) 
resultado3 = int(soma3/3)

print(f"Os resultados da media são: \n" 
      f"(Primeira media: {resultado1}\n"
      F"{resultado2}\n" 
      F"{resultado3}\n")

media = [resultado1,resultado2,resultado3]
print("O maior valor das medias digitadas é: ")
maior = max(media)

        
print(maior)
print("")
