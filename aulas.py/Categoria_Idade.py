
nome =str (input("Nome do atleta:"))
idade = int (input("Idade do Atleta:"))

match idade:
    case 5|6|7|8|9|10:
        categoria = "Infantil"
    case 11|12|13|14|15:
        categoria = "Juvenil"
    case 16|17|18|19|20:
        categoria = "junior"
    case 21|22|23|24|25:
        categoria = "Profissional"    
    case _:
        categoria = "Invalida"
    
print(f"{nome} sua categoria é {categoria}")   
