print("Para somar os numero aperte 0")
print("")
soma = 0
# inicializa a variável soma com 0


n = int(input("Digite um numero: "))
# lê um número do usuário e converte para inteiro


while n != 0:
    # enquanto o número digitado não for zero
    soma = soma + n
    # adiciona o valor digitado à soma acumulada
    n = int(input("Digite um numero: "))
    # pede outro número para continuar a soma

print(f"A soma dos numeros é: {soma}")
# exibe o resultado final da soma