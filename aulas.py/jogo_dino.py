import os
import time
import random
import msvcrt #Biblioteca padrao do windows para ler no teclado sem pausar o jogo


#configurações do jogo  / onde o dinossauro fica fixo no chao
LARGURA_PISTA = 30
posicao_dino = 3   
chao = " " * LARGURA_PISTA

#VARIAVEL DE ESTADO DO JOGO / guarda a posição dos cactos
dino_chao = True
tempo_pulo = 0
cactos = []
pontos = 0
jogador = True

print("===JOGO DO DINO NO TERMINAL===")
print("PRECIONE O ESPAÇO PARA PULAR!")
print("PRESSIONE QUALQUER TECLA PARA COMEÇAR...")
msvcrt.getch()

#LOGO PRINCIPAL 
while  jogador: # Limpa a tela do terminal p/ fazer a animação
    os.system("cls" if os.name == "nt" else "clear")

    #Controla o tempo que fica no ar ou seja o PULO
    if not dino_chao: 
        tempo_pulo +=1
        if tempo_pulo >3: # FICA RODANDO NO AR E DESCE
            dino_chao = True
            tempo_pulo = 0   

    # lê o teclado : se apertou o espaço  e esta no chão , pulka,
    if msvcrt.kbhit():
        tecla = msvcrt.getch()
        if tecla == b" " and dino_chao:
            dino_chao = False

    #Movimenta os cactos para esquerda
    novos_cactos = []
    for cacto in cactos:
        if cacto > 0 :
            novos_cactos.append(cacto - 1)  
        else:
            pontos += 1 # Se o cacto sair da sua tela ganhou os pontos
    cactos = novos_cactos

    # Cria aleatoriamente novos cactos a direita
    if random.randint(1,10) == 1 and (len(cactos) == 0 or cactos[-1] < LARGURA_PISTA -8):
        cactos.append(LARGURA_PISTA - 1)

    # Verifica se teve a colisão (Game Over)
    # Se tem um cacto na mesma posição que o dino, o dino esta no chão... batida!  
    if posicao_dino in cactos and dino_chao:
        print("\n" *3)  
        print(" 💥  GAME OVER! 💥") 
        print(f"Pontuação Final: {pontos}")  
        break

    # Desenha o cenário no terminal
    # Linha do ar / entre o pulo e o chão 
    linha_ar = [" "] * LARGURA_PISTA
    if not dino_chao:
        linha_ar[posicao_dino] = "D"
    print("".join(linha_ar))

    #linha do chão (onde fica os cactos parados)   
    linha_chao = ["_"] * LARGURA_PISTA
    if dino_chao:
        linha_chao[posicao_dino] = "D"

    #coloque os cactos na pista
    for  cacto in cactos:
        linha_chao[cacto] = "X"   
    print("".join(linha_chao))  

    #Mostrar placar
    print(f"\nPontos:{pontos}") 

    #Controle de velocidade
    time.sleep(0.1)  




