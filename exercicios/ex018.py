from math import hypot # uso o from math pois usa a função especifica
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente :"))
h = hypot(co,ca) #h = (co ** 2 + ca ** 2) ** (1/2)
print(f"A hipotenusa vai medir: {h:.2f} ")


