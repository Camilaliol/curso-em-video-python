import random
import pygame

# Inicia a ferramenta do pygame
pygame.init()

# Configura as dimensões da nossa arena
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("<<<<<<<<< JOGO DA COBRINHA >>>>>>>>>>")

# Definindo as cores (padrão RGB)
PRETO = (15, 15, 20) # cor do fundo
VERMELHO = (255, 40, 40) 
DOURADO = (255, 215, 0) # Cor da maçã bónus
BRANCO = (255, 255, 255) # CORREÇÃO: Adicionado novamente pois é usada no placar e bónus

# Cores secretas para os efeitos visuais
VERDE = (0, 255, 0) # VERDE LIMÃO  
VERDE_CABECA = (0, 150, 0) # Verde escuro para dar contraste
VERDE_RABO = (0, 80, 0) # Onde começa o degradê do rabo
BRILHO_MACA = (255, 100, 100) # Cor clara para dar um reflexo de luz

# Tamanho E VELOCIDADE da nossa cobrinha 
TAMANHO_BLOCO = 20
cobra_x = LARGURA / 2 # Começa no meio da tela (Posição inicial)
cobra_y = ALTURA / 2
velocidade_x = 0 # Ela inicia parada 
velocidade_y = 0
cobra_corpo = [] # lista vazia que guarda os segmentos da cobra
comprimento_cobra = 1 # A cobra começa apenas com 1 bloco 

# Posição inicial da comida
comida_x = random.randrange(0, LARGURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
comida_y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)

# Controla a velocidade de atualização (FPS)
relogio = pygame.time.Clock()

# SISTEMA DE FONTES
fonte_placar = pygame.font.SysFont("arial", 25, bold=True) # FONTE DO PLACAR
fonte_game_over = pygame.font.SysFont("arial", 35, bold=True) # FONTE DO GAME OVER
fonte_subtitulo = pygame.font.SysFont("arial", 20, bold=True)

# Criando a função Placar
def mostrar_placar(pontos):
    texto = fonte_placar.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, [10, 10])

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
    velocidade_base = 10 

    comida_x = random.randrange(0, LARGURA - TAMANHO_BLOCO, TAMANHO_BLOCO) 
    comida_y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)

    # VARIÁVEL BÓNUS
    comida_bonus_x = 0
    comida_bonus_y = 0
    bonus_ativo = False
    tempo_bonus_restante = 0

    game_over = False # Controle se o jogador perdeu nesta jogada

    # Loop da partida inicial
    while not game_over and rodando:        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            # Se o jogador apertar uma tecla:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and velocidade_x == 0:
                    velocidade_x = -TAMANHO_BLOCO
                    velocidade_y = 0
                elif evento.key == pygame.K_RIGHT and velocidade_x == 0:
                    velocidade_x = TAMANHO_BLOCO
                    velocidade_y = 0
                elif evento.key == pygame.K_UP and velocidade_y == 0: # CORREÇÃO: trava vertical ajustada para y
                    velocidade_y = -TAMANHO_BLOCO
                    velocidade_x = 0
                elif evento.key == pygame.K_DOWN and velocidade_y == 0: # CORREÇÃO: trava vertical ajustada para y
                    velocidade_y = TAMANHO_BLOCO
                    velocidade_x = 0

        # CORREÇÃO DE INDENTAÇÃO: Todo este bloco voltou para dentro do loop da partida activa
        # Atualizando a posição da cobra com base na velocidade
        cobra_x += velocidade_x
        cobra_y += velocidade_y

        # Guarda a posição atual da cabeça
        cabeca = [cobra_x, cobra_y]
        cobra_corpo.append(cabeca)

        # Se a lista ficou maior que o tamanho permitido, apaga o rabo
        if len(cobra_corpo) > comprimento_cobra:
            del cobra_corpo[0]

        # Novo GAME OVER: Se a cabeça bater no próprio corpo!
        for segmento in cobra_corpo[:-1]: 
            if segmento == cabeca and (velocidade_x != 0 or velocidade_y != 0):
                print("BATEU NO PRÓPRIO CORPO! 💥 GAME OVER! 💥")
                game_over = True

        # Detectar as paredes
        if cobra_x >= LARGURA or cobra_x < 0 or cobra_y >= ALTURA or cobra_y < 0:
            print("BATEU NA PAREDE! 💥 GAME OVER! 💥 ") 
            game_over = True

        # Colisão com a comida
        if cobra_x == comida_x and cobra_y == comida_y:
            comida_x = random.randrange(0, LARGURA - TAMANHO_BLOCO, TAMANHO_BLOCO) 
            comida_y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
            comprimento_cobra += 1

            # Sorteio da Maçã Dourada
            if not bonus_ativo and random.random() < 0.20:
                comida_bonus_x = random.randrange(0, LARGURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
                comida_bonus_y = random.randrange(0, ALTURA - TAMANHO_BLOCO, TAMANHO_BLOCO)
                bonus_ativo = True
                tempo_bonus_restante = 50 
                
            pontos_atuais = comprimento_cobra - 1
            nivel_atual = (pontos_atuais // 5) + 1
            print(f"Comi! Pontos: {pontos_atuais} | Nível: {nivel_atual}")
        
        # Lógica de tempo da Maçã Dourada
        if bonus_ativo:
            tempo_bonus_restante -= 1
            if tempo_bonus_restante <= 0:
                 bonus_ativo = False 

            if cobra_x == comida_bonus_x and cobra_y == comida_bonus_y:
                comprimento_cobra += 3 
                bonus_ativo = False
                print("💥 MAÇÃ DOURADA! +3 PONTOS! 💥")    
        
        # LIMPEZA E DESENHO DAS MAÇÃS
        tela.fill(PRETO)

        raio = TAMANHO_BLOCO // 2
        centro_comida_x = comida_x + raio
        centro_comida_y = comida_y + raio

        # Desenha a maçã normal vermelha com brilho
        pygame.draw.circle(tela, VERMELHO, (centro_comida_x, centro_comida_y), raio)
        pygame.draw.circle(tela, BRILHO_MACA, (centro_comida_x - 3, centro_comida_y - 3), 3) # CORREÇÃO: centro_comida_x aplicado

        # Se o bónus estiver ativo, desenha a maçã dourada circular
        if bonus_ativo:
            centro_bonus_x = comida_bonus_x + raio
            centro_bonus_y = comida_bonus_y + raio
            # CORREÇÃO: Alinhamento das linhas de desenho ajustadas
            pygame.draw.circle(tela, DOURADO, (centro_bonus_x, centro_bonus_y), raio)
            pygame.draw.circle(tela, BRANCO, (centro_bonus_x, centro_bonus_y), raio - 4, 1)

        for indice, segmento in enumerate(cobra_corpo):    
            if indice == len(cobra_corpo) - 1:
                # CORREÇÃO: Usar segmento[0] e segmento[1] para X e Y
                pygame.draw.rect(tela, VERDE_CABECA, [segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO], border_radius=7)

                # Coordenadas padrão olhando para a frente
                o1_x, o1_y = segmento[0] + 5, segmento[1] + 5
                o2_x, o2_y = segmento[0] + 15, segmento[1] + 5

                # Altera os eixos dinamicamente consoante o movimento
                if velocidade_x > 0: # Movimento para a direita
                    o1_x, o1_y = segmento[0] + 14, segmento[1] + 4 
                    o2_x, o2_y = segmento[0] + 14, segmento[1] + 14
                elif velocidade_x < 0: # Movimento para a esquerda
                    o1_x, o1_y = segmento[0] + 4, segmento[1] + 4
                    o2_x, o2_y = segmento[0] + 4, segmento[1] + 14
                elif velocidade_y > 0: # CORREÇÃO: Adicionados os dois pontos ':' que faltavam
                    o1_x, o1_y = segmento[0] + 4, segmento[1] + 14
                    o2_x, o2_y = segmento[0] + 14, segmento[1] + 14

                # Desenha os olhos
                pygame.draw.circle(tela, BRANCO, (int(o1_x), int(o1_y)), 3)    
                pygame.draw.circle(tela, BRANCO, (int(o2_x), int(o2_y)), 3)
                pygame.draw.circle(tela, PRETO, (int(o1_x), int(o1_y)), 1)
                pygame.draw.circle(tela, PRETO, (int(o2_x), int(o2_y)), 1) # CORREÇÃO: Mudado dray para draw

            else:
                
                fator = indice / len(cobra_corpo)
                cor_r = int(VERDE_RABO [0] + (VERDE[0] - VERDE_RABO[0]) * fator)
                cor_g = int(VERDE_RABO [1] + (VERDE[1] - VERDE_RABO[1]) * fator)
                cor_b = int(VERDE_RABO [2] + (VERDE[2] - VERDE_RABO[2]) * fator)
                pygame.draw.rect(tela, (cor_r, cor_g, cor_b), [segmento[0] + 1, segmento[1] + 1, TAMANHO_BLOCO - 2, TAMANHO_BLOCO - 2], border_radius=4)

        # DESENHANDO O PLACAR NA TELA
        mostrar_placar(comprimento_cobra - 1)

        pygame.display.update()
        relogio.tick(velocidade_base + (nivel_atual - 1) * 2) 

    # TELA DE GAME OVER GRANDE 
    while game_over and rodando:
        tela.fill(PRETO)

        texto_go = fonte_game_over.render("💥 GAME OVER! 💥", True, VERMELHO)   
        texto_pontos = fonte_subtitulo.render(f"Você fez {comprimento_cobra - 1} pontos! (Nivel {nivel_atual}) ", True, BRANCO) 
        texto_opcoes = fonte_subtitulo.render("Pressione [C] para Jogar de Novo ou [Q] para Sair", True, BRANCO)

        tela.blit(texto_go, [LARGURA / 2 - 110, ALTURA / 2 - 60])
        tela.blit(texto_pontos, [LARGURA / 2 - 130, ALTURA / 2 - 10])
        tela.blit(texto_opcoes, [LARGURA / 2 - 210, ALTURA / 2 + 30])

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                game_over = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q: 
                    rodando = False
                    game_over = False
                if evento.key == pygame.K_c: 
                    game_over = False        

pygame.quit()