frase = input(
    "Digite uma frase: "
).upper()  # lê a frase digitada e converte tudo para maiúsculas
quant = frase.count("A")  # conta quantas letras A existem na frase
prima = (
    frase.find("A") + 1
)  # encontra a posição da primeira letra A (índice começa em 0)
ultima = frase.rfind(
    ("A") + 1
)  # encontra a posição da última letra A (esta linha está errada; rfind espera só uma string)
print(
    f"A letra A apareceu {quant} vezes na frase."
)  # exibe quantas letras A foram encontradas
print(
    f"A primeira letra A apareceu na posição {prima}"
)  # mostra a posição da primeira ocorrência de A
print(
    f"A última letra A apareceu na posição {ultima}"
)  # mostra a posição da última ocorrência de A
