from random import choice #escolha aleatoria
a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str (input("Quarto aluno: "))

alunos = [a1, a2, a3, a4] #crie uma lista

sorteados = choice(alunos) #random.choice ele randomiza, ele escolhe uma valor 
print(f"O aluno sorteado foi {sorteados}")


