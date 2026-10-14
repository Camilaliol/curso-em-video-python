from xmlrpc.client import boolean


print("|----------------------------------|")
print("|             DOAÇÕES              |")
print("|----------------------------------|")
print("|       FAÇA SUA DOAÇÃO            |")
print("|----------------------------------|")
print("|             DOAÇÕES              |")
print("|                                  |")
print("|(1) PARA DOAR 10€                 |")
print("|(2) PARA DOAR 20€                 |")
print("|(3) PARA DOAR 50€                 |")
print("|(4) PARA DOAR OUTROS VALORES      |")
print("|(5) PARA SAIR SEM DOAR            |")
print("|----------------------------------|")


opcao = int(input("Escolha uma doação: "))
match opcao:
    case 1:
        doar = 10
    case 2:
        doar = 20
    case 3:
        doar = 50
    case 4:
        doar = boolean(input("Qual o valor voê gostaria de doar:"))
    case 5:
        doar = 0

input(f"Você doou {doar},00€ !,muito Obrigada por sua doação")

