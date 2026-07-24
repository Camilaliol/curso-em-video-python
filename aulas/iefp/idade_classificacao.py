age = int(input("Qual a sua idade ? "))

if age <= 4:
    print(f"Você tem {age} anos. É um bebé 👶 ")
elif age <=13:
    print(f"Você tem {age} anos.é uma criança 👧👦 ")
elif age <=18:
    print(f"Você tem {age} anos. é um adolecente 🛉 ")   
elif age <= 65:
    print(f"Você tem {age} anos. é um adulto 🧍 ")  
elif age <=100:
    print(f"Você tem {age} anos. É um idoso🧓 ")
else:
    print(f"Você tem {age}anos. É muito velho 👴 ")       
    