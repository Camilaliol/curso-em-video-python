V1 = []
V2= []
total = []

for i  in range (2):
    valor = int(input("numero 1:"))
    V1.append (valor)
    valor = int(input("numero 2:"))
    V2.append (valor)

totav1 = sum(V1)
totav2 = sum(V2)

total.append(totav1 + totav2)

print(f"A soma total é {total}")    
 
    