nome = input("Digite o seu nome completo:")  # lê o nome completo digitado pelo usuário
primeiro = nome.split()[0]  # divide o nome em palavras e pega a primeira palavra
ultimo = nome.split()[-1]  # divide o nome em palavras e pega a última palavra
print("------Muito Prazer em te conhecer! ----------")
print(f"Seu primeiro nome é {primeiro}")
print(f"Seu útimo nome é {ultimo}")
