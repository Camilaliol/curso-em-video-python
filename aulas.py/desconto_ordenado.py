nome = str(input("Escreva Seu nome: "))
ordenado = int(input("Escreva o valor do seu salario: "))

if ordenado <= 500:
    desc = ordenado * 0.01
    print(f"Com o valor de salario de {ordenado} o valor a ser descontado sera: {desc} €")

elif ordenado <= 1000:
    desc = ordenado * 0.02
    print(f'Com o valor de salario de {ordenado} o valor a ser descontado sera: {desc} €')

elif ordenado <= 4000:
    desc = ordenado * 0.03
    print(f'Com o valor de salario de {ordenado} o valor a ser descontado sera: {desc} €') 

else:    
    desc = ordenado * 0.04
    print(f'Com o valor de salario de {ordenado} o valor a ser descontado sera: {desc} €') 

