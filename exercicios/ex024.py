numero = int(
    input("Digite um numero:")
)  # lê o número digitado pelo usuário e converte para inteiro

print(f"    Analisando o numero {numero}............")  # exibe o número informado

unidade = numero // 1 % 10  # divide por 1 e pega o resto de 10: último dígito
dezena = numero // 10 % 10  # remove a unidade e pega o próximo dígito
centena = numero // 100 % 10  # remove unidades e dezenas e pega o dígito das centenas
milhar = (
    numero // 1000 % 10
)  # remove os três últimos dígitos e pega o dígito dos milhares

print(f"Unidade: {unidade}")  # imprime o dígito das unidades
print(f"Dezena: {dezena}")  # imprime o dígito das dezenas
print(f"Centena: {centena}")  # imprime o dígito das centenas
print(f"Milhar: {milhar}")  # imprime o dígito dos milhares
