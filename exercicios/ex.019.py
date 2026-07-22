from math import sin,cos,tan,radians,tan
an = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print(f"O ângulo de {an} tem o seno de: {seno:.2f} ")
print(f"O ângulo de {an} tem o cosseno de: {cosseno:.2f} ")
print(f"O ângulo de {an} tem o tangente de: {tangente:.2f} ")


