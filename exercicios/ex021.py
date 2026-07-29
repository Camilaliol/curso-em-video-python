from random import shuffle
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro Aluno: "))
a4 = str(input("Quarto Aluno: "))

aluno = [a1,a2,a3,a4]
ordem = shuffle(aluno) #Modifica a ordem da lista original diretamente na memoria
print(f"A ordem de apresntação será: {aluno}")

