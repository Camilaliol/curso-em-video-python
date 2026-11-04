soma = 0 
quantidade = 0

print("Digite quantos numeros quiser para fazer a media ")
print("Para terminar a conta , digite um numero negativo")
print("________________________________________________ ")


while True:

    numero = int(input("Digite um numero inteiro:     "))

    if numero < 0: #local onde informa que se o numero for menor que 0 deve sair do programa
        break
    soma = soma + numero
    quantidade = quantidade +1
print("_________________________________________________")

if quantidade > 0:
    media = soma / quantidade
    print(f"A media dos numeros digitados é {media:.2f} ")

else:
    print("Nenhum número positivo foi digitado.        ")

