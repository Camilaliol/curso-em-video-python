# Cria uma lista com os números, guardados como textos.
n = ["1","6","7","10","15"]

# Converte cada elemento para inteiro e calcula a soma dos números.
soma = int(n[0]) + int(n[1]) + int(n[2]) + int(n[3]) +int(n[4])
print(f"A soma dos numeros é: {soma}")

# Mostra uma mensagem antes de apresentar a lista invertida.
print("Os numero ao contrário são:")

# Inverte a ordem dos elementos da lista.
n.reverse()
print(n)

for n in n:

    if n % 2 == 0:
        print(f"Os numero pares são {n}")

