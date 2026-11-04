idade = 0
menor_21 = 0
maior_50 = 0

print("Informe varias idade  ")
print("Para sair aperte 0    ")
print(" _____________________")
print("                      ")

while True:
    idade = int(input("Digite a idade: "))

    if idade == 0:
        break

    if idade < 21:
        menor_21 = menor_21 + 1
        

    if idade > 50:
        maior_50 = maior_50 + 1    
        

print(f"O numero de pessoas com menos de  21 anos é {menor_21}")
print(f"O numero de pessoas com mais de 50 anos é {maior_50}")  
