carteira = float(input("Quanto dinheiro você tem na carteira? R$ "))
dolar = carteira / 5.09 #dolar/real
euro = carteira / 5.82 
print("---" *12) #print para criar caractere no codigo
print(f"Com R$ {carteira} você pode comprar US$ {dolar:.2f}")
print(f"Com R$ {carteira} voce pode comprar   € {euro :.2f} ")
print("---" *12)




