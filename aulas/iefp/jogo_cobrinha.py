import random
import pygame

#Inicia a ferramente do pygame
pygame.init()

#Configura as dimençoes da nossa arena
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption ("JOGO DA COBRINHA")

#Definindo as cores (padrão RGB)
PRETO = (0,0,0)
VERDE = (0,255,0)
VERMELHO = (255,0,0)
BRANCO = (255,255,255)
DOURADO = (255,215,0)

#Tamanho E VELOCIDADE da nossa cobrinha 
TAMANHO_BLOCO = 20
cobra_x = LARGURA / 2 #Começa no meio da tela (Posição inicial)
cobra_y = ALTURA / 2
velocidade_x = 0 # Ela inicia parada 
velocidade_y = 0
cobra_corpo = [] # lista vazia que guarda os seguimento da cobra
comprimento_cobra = 1 # A cobra começa apenas com 1 bloco 

#Posiçãp inicial da comida (Precisa ser add para o jogo funcionar)
comida_x = random.randrange(0, LARGURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
comida_y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)

# Controla a velocidade de arualização (FPS)
relogio = pygame.time.Clock()

#  SISTEMA DE FONTES
fonte_placar = pygame.font.SysFont("arial", 25, bold=True) # FONTE DO PLACAR
fonte_game_over = pygame.font.SysFont ("arial", 35, bold=True) # FONTE DO GAME OVER
fonte_subtitulo = pygame.font.SysFont("arial", 20, bold=True)

#Criando a funçao Placar
def mostrar_placar(pontos):
    #Criando a imagem do texto
    texto = fonte_placar.render(f"Pontos: {pontos}", True, BRANCO)
    #Desenha o texto na cordenadas x=10, y=10 (canto superior esquerdo)
    tela.blit(texto,[10,10])

# O loop principal (apenas um único coração para o jogo)
rodando = True

while rodando:
    # RESET DE VARIÁVEL PARA REINICIAR O JOGO
    cobra_x = LARGURA / 2
    cobra_y = ALTURA / 2
    velocidade_x = 0
    velocidade_y = 0
    cobra_corpo = []
    comprimento_cobra = 1
    nivel_atual = 1
    velocidade_base = 10 # 10 atualizaçoes por minuto

    comida_x = random.randrange(0, LARGURA - TAMANHO_BLOCO, TAMANHO_BLOCO) 
    comida_y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)

    # VARIAVEL BÓNUS
    comida_bonus_x = 0
    comida_bonus_y = 0
    bonus_ativo = False
    tempo_bonus_restante = 0

    game_over = True # Controle se o jogador perdeu nesta codada

    #Loop da partida inicial
    while not game_over and rodando:        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            #Se o jogador apertar uma tecla:
            if evento.type == pygame.KEYDOWN:
            
                if evento.key == pygame.K_LEFT:
                    velocidade_x = -TAMANHO_BLOCO
                    velocidade_y = 0

                elif evento.key == pygame.K_RIGHT:
                    velocidade_x = TAMANHO_BLOCO
                    velocidade_y = 0

                elif evento.key == pygame.K_UP:
                        velocidade_y = -TAMANHO_BLOCO
                        velocidade_x = 0

                elif evento.key == pygame.K_DOWN:
                    velocidade_y = TAMANHO_BLOCO
                    velocidade_x = 0

    #Atualizando a posição da cobra com base na velocidade
        cobra_x += velocidade_x
        cobra_y += velocidade_y

    #Guarda a posição atual da cabeça
        cabeca = [cobra_x, cobra_y]
        cobra_corpo.append(cabeca)

    #Se a lista ficou maior que o tamanho permitindo, apaga o rabo
        if len(cobra_corpo) > comprimento_cobra:
            del cobra_corpo[0]

    # Novo GAME OVER: Se a cabeça bater no proprio corpo!
        for segmento in cobra_corpo[:-1 ]: #Olha para todos os segmentos, exceto a cabeça 
            if segmento == cabeca and (velocidade_x != 0 or velocidade_y !=0):
                print("BATEU NO PROPRIO CORPO! 💥 GAME OVER! 💥")
                rodando = False

    #detectar as paredes
        if cobra_x >= LARGURA or cobra_x < 0 or cobra_y >= ALTURA or cobra_y < 0:
            print("BAREU NA PAREDE! 💥 GAME OVER! 💥 ") 
            rodando = False 
    
       

    # Colisao com a comida
        if cobra_x == comida_x and cobra_y == comida_y:
            comida_x = random.randrange(0, LARGURA - TAMANHO_BLOCO, TAMANHO_BLOCO) 
            comida_y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
            comprimento_cobra += 1

            #  SORTEIO DA MAÇA DOURDA
            if not bonus_ativo and random.random() < 0.20:
                comida_bonus_x = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
                comida_bonus_y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
                bonus_ativo = True
                tempo_bonus_restante = 50 # 5a frames a 10 FPS
                # calculo do nivel
                #Se pontos (comprimento -1) for 0,1 ou 2 -> Nivel 1
                 #Se pontos for 3,4 ou 5 -> Nivel 2(3 // 3 = 1 +1 = 2)
            pontos_atuais = comprimento_cobra -1
            nivel_atual = (pontos_atuais // 5) + 1
            print(f"Comi ! Pontos : {pontos_atuais} | Nível: {nivel_atual}")
        
        # LO9GICA DE TEMPO E COMPORTAMENTO DA MAÇÃ DOURADA
        if bonus_ativo:
            tempo_bonus_restante -= 1
            if tempo_bonus_restante <=0:
                 bonus_ativo = False #Se o tempo acabar ela some

            if cobra_x == comida_bonus_x and cobra_y == comida_bonus_y:
                comprimento_cobra += 3 # Ganha +3 blocos de uma so vez.
                bonus_ativo = False
                print("💥 MAÇÃ DOURADA! +3 PONTOS! 💥")    
        
        tela.fill(PRETO)

    #Desenho da comida (retândulo vermelho)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO])

    #Desenha todos os segmentos da cobra
        for indice,segmento in enumerate(cobra_corpo) :
            if indice == len (cobra_corpo) -1:
                #Mudando a cor da cabeça
                COR_CABECA = (0,180,0) 
                pygame.draw.rect(tela,VERDE, [segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO])
        
            else:
                # Configurando a cor e tamanho do corpo
                pygame.draw.rect(tela, VERDE, [segmento[0] + 1, segmento[1] + 1, TAMANHO_BLOCO - 2, TAMANHO_BLOCO - 2])            

        #DESENHANDO O plACAR NA TELA
        mostrar_placar(comprimento_cobra - 1)

        pygame.display.update()

        #       VELOCIDADE DINAMICA
        # NIVEL 1: 10 +(0 * 2) = 10 fps
        # NIVEL 2: 10 +(1 * 2) = 12 FPS
        # NIVEL 3: 10 +(2 * 2) = 14 FPS
        relogio.tick(velocidade_base + (nivel_atual - 1) * 2) 

        #    TELA DE GAME OVER GRANDE 
    while game_over and rodando:
        tela.fill(PRETO)

        texto_go = fonte_game_over.render("💥 GAME OVER! 💥", True, VERMELHO)   
        texto_pontos = fonte_subtitulo.render(f"Você fez{comprimento_cobra - 1} pontos! (NIvel{nivel_atual})", True, BRANCO) 
        texto_opcoes = fonte_subtitulo.render("Pressione [C] para Jogar de NOvo ou [Q] para Sair",True, BRANCO)

        tela.blit(texto_go, [LARGURA / 2 - 110, ALTURA / 2 - 60])
        tela.blit(texto_pontos, [LARGURA / 2 - 130, ALTURA / 2 - 10])
        tela.blit(texto_opcoes, [LARGURA / 2 -210, ALTURA / 2 + 30])

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                game_over = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q: # O Q serve para fechar o jogo
                    rodando = False
                    game_over = False

                if evento.key == pygame.K_c: # O C serve para reiniciar do zero
                    game_over = False        

pygame.quit()    