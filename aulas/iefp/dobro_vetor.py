limite = 5
lista = []

for i in range (10):
    if len(lista) < limite:
        valor = int(input("numero para add numero na lista do vetor: "))
        lista.append(valor)

    else:
        print("Lista já cheia")   
        break

print(f"A lista {lista} ")     

