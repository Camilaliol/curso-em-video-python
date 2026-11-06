lista = []

while True:
    valor = input("Digite um numero ou Sair pra encerrar: ")
    #lower para escrever em maiusculo ou minusculo

    if valor.lower() == "sair":
        break
    
    lista.append(int(valor))

print(f"Minha lista {lista[::-1]}")    # o numero -1 faz como que a lista seja apresentada ao contratio