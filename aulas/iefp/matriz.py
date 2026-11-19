#Declaração de uma matriz vazia com 4 linhas e 3 colunas (preenchida com zeros)
matriz = [[0 for _ in range(3)] for _ in range(4)]

#Preencher a matriz com dados digitados
for linha in range(4):
    for coluna in range(3):
        numero = int(input(f"Digite um numero para [{linha}], [{coluna}] :"))
        matriz[linha] [coluna ] = numero
#Escrever um elemento da matriz no ecãm(Linha 0. coluna1)
print(matriz[0][1])        