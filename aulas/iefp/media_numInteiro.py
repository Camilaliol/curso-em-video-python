while True:

    soma = 0 
    quantidade = 0

    print("\n--- NOVO CÁLCULO DE MÉDIA ---")
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

    continuar = input("Quer continuar a calcular ? (S para sim ou aperte qualquer numero negativo para sair):").upper()

    if continuar != 'S':  
        print("Obrigada por usar o programa! Até à próxima")    
    break      


