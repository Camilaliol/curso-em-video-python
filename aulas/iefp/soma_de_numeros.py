n = int(input("Digite um numero: "))

contador = 1
soma = 0

while contador <= n:
    print(contador, end="")

    soma = soma + contador

    if contador < n:
        print(" + ", end="")
    contador = contador + 1


print(" = ", soma)
