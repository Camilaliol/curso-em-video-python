larg = float(input("Escreva a largura :"))
height = float(input("Escreva a altura: "))
area = larg * height 
tinta = area / 2
print(f"Sua parede tem a dimensão de  {larg:.2f} x {height:.2f} e sua área total é {area:.2f}m2")
print(f"Para pintar essa parede de {area}m2, você precisará de {tinta:.2f}l de tinta")
