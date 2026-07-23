aluno = str(input( "Escreva o nome do aluno: "))
nota = float(input("Digite a nota do Aluno: "))

while nota < 0 or nota > 20:
    print("Nota inválida! Digite um valor de 0 a 20.")
    nota= float(input("Digite a nota do aluno :"))

print(f"A nota do aluno (a) {aluno} foi: {nota} ")

if nota <= 10:
    print(f"{aluno} foi pessimo. Você precisa estudar muito ")
elif  nota <=15:
    print(f"{aluno} você esta na média. Você precisa estudar mais ")
else:
    print(f"{aluno} Parabéns você foi aprovado")
    #print("Nota fora dos intervalos especificados")

        