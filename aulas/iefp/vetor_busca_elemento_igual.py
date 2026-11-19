v = [10, 25, 30, 45, 50]
n = len(v)

i = 0
enc = 0
elen = int(input("Digite o valor a pesquisar: "))

while i < n and enc == 0:
    if v[i] == elen:
        enc = 1
    else:
        i = i +1

    if enc == 1:
         print(f"O elemento {elen} está ma posição {i +1}")

    else:
        print(f"O elemento {elen} não existe no vetor")             