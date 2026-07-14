tab = int(input("Escreva um numero para ver a tabuada: "))
print("_" * 12)
#o range (1,11) gera a seguencia 1 a 10 (o segundo numero nunca é incluido)
for i in range(1,11):
    resultado = tab * i
    print(f"{tab} x {i:2} = {resultado}")
print("_" * 12)    
