limite_lista = 5 # numero maximo da lista

lista = []

for i in range (10): #como houve a limitação o inicio o range n chegara a 10
    
    if len (lista) < limite_lista:
        valor = int(input("NUmero para adicionar a lista:"))
        lista.append(valor)

    else:
        print("lista cheia")   
        break 

print(lista)   



