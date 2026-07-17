n = str(input("Digite o seu nome ? "))
nascimento = int(input("Qual o seu ano de nascimento :"))
anoA = int(input("Qual é o ano atual: "))
idade =  anoA - nascimento
print(f"A idade de {n} é {idade} anos")
if idade >= 18:
    print("Parabens você é maior e idade")
else: 
    print("Você ainda não atingiu a maior idade")




 