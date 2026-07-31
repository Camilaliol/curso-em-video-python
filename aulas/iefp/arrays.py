# Lista vazia onde vamos guardar as respostas.
nomes = []

# Pede a quantidade e converte a resposta para um número inteiro.
quantidade = int(input("Digite quantos nomes voce quer inserir: "))

# Repete a pergunta a quantidade de vezes escolhida.
for indice in range(quantidade):
   nome = input(f"Digite o nome {indice + 1}: ")
   nomes.append(nome)  # Adiciona a resposta à lista.

print(f"A lista de nomes: {nomes}")

# Mostra cada nome da lista em uma linha.
for nome in nomes:
   print(nome)