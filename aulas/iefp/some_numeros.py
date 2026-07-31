# Pede três números ao utilizador e converte cada resposta para inteiro.
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

# Começamos a soma em zero.
soma = 0

# Adicionamos cada número à soma anterior.
soma = soma + n1
soma = soma + n2
soma = soma + n3

# Mostra o resultado final.
print("=", soma)