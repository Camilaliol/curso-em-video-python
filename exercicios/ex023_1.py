nome = input("Digite o seu nome correto: ").strip()
# strip() remove espaços no início e no fim da entrada

print("Analisando seu nome .......")
print(f"Seu nome em maiúsculo é {nome.upper()}")
# upper() transforma todas as letras em maiúsculas

print(f"Seu nome em minúsculo é {nome.lower()}")
# lower() transforma todas as letras em minúsculas

print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras")
# len(nome) conta todos os caracteres,
# nome.count(' ') conta quantos espaços há,
# assim subtrai-se os espaços para contar apenas letras

print(f"Seu primeiro nome tem {nome.find(' ')} letras.")
# find(' ') retorna a posição do primeiro espaço,
# que equivale ao número de letras do primeiro nome
# (se não houver espaço, retorna -1)