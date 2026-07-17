dia = int(input("Quantos dias alugados ? "))
km = float(input("Quantos Km rodados ? "))
pago = dia * 60
roda = km * 0.15
total = pago + roda
print(f"O total a pagar é R$ {total:.2f}")
