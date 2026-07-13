tab = int(input("Escreva um numero para ver a tabuada: "))
#o range (1,11) gera a seguencia 1 a 10 (o segundo numero nunca é incluido)
for i in range(1,11):
    resultado = tab * i
    print(f"{tab} x {i} = {resultado}")
