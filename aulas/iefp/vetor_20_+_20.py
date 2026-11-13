import random 
limite_lista = 40 #limite a apenas 40

vetor1 = []
vetor2 = []
vetor3 = []

for i in range (20):
   
   if len (vetor1) < limite_lista:
    numero = random.randint(1,100)
    #valor = (int(input(numero)))
    vetor1.append(numero)

for i in range (20):
   
   if len (vetor2) < limite_lista:
    numero = random.randint(1,100)
    #valor = (int(input(numero)))
    vetor2.append(numero)

vetor3 = vetor1 + vetor2   

print(vetor1)
print("_________________________________________________")

print(vetor2)

print("_________________________________________________")
print(vetor3)

print("_________________________________________________")
