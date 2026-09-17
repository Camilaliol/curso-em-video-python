dados = [] 
while True: 
    valor = input ("Digite os gastos: ou digite sair" )
    
    if valor.lower()=="sair":
        break
    dados.append(int(valor))
total = sum (dados)

print (dados,total)