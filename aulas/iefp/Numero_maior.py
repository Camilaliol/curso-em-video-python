maior_numero = 0 
print('Digite quantos numeros quiser. Para sair aperte 0: ')

# cria um llop infinito o While True
while True:
    n1 = int(input('Digite um numero: '))

    #Opção de saida do programa/ == limita a sempre que for = 0 ele sai do programa
    if n1 == 0:
        break # obrigta a sair do loop

     # faz a comparação ente os numeros digitados   
    if n1 > maior_numero:
        maior_numero = n1

print(f"O maior numero foi: {maior_numero} ")        


