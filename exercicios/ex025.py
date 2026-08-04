n = input("Escreva o seu nome completo: ")  # lê o nome completo digitado pelo usuário
nc = (
    "silva" in n.lower()
)  # verifica se a palavra 'silva' está no nome, ignorando maiúsculas/minúsculas
print(
    f"Seu nome tem Silva? {'Sim' if nc else 'Não'}"
)  # mostra o resultado ao usuário como Sim ou Não
