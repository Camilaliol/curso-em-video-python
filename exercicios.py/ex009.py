# Esse programa converte metros em centimetros.

# Lê o input do usuário e armazena na variável `metros`.
metros = float(input("Escreva a medida em metros:  "))

# Converte a variável `metros` em `centimetros` multiplicando por 100.
centimetros = metros * 100
milimetros = metros * 1000

# Escreve o input inicial e o valor calculado centimetros.
print(f"{metros} metros equivalem a {centimetros} cm.")
print(f" {metros} metros equivalem a {milimetros} ml ") 
