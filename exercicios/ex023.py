nome = input("Digite o seu nome:")
nome_formatado = nome.strip().title()
nome_sem_espaco = nome.replace(" ","")
total_letras = len(nome_sem_espaco)
primeiro_nome = nome.strip().split()[0]
letra_primeiro_nome = len(primeiro_nome)

print(f"Nome formatado: {nome_formatado}")
print(f"Total de letras sem espaço: {total_letras}")
print(f"Letras do primeiro nome: {letra_primeiro_nome}")





