import pygame
import random  # importando o random para fazer o ecrã vibrar

#TAMANHO DA TELA
LARGURA = 800
ALTURA = 600
TITULO = "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< BRICK BREAKER >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

# PALETA DE CORES  
COR_FUNDO = (20,24,36)
COR_BORDA = (50,60,85)
COR_BARRA = (0, 200, 255)
COR_BOLA = (255, 255, 255) # BRANCO BRILHANTE
COR_TEXTO = (240, 240, 240)
COR_VITORIA = (46, 213, 115)
COR_DERROTA = (255,75,92)

#COR DOS BLOCOS
CORES_BLOCOS = [
    (255, 75, 92), # VERMELHO CORAL
    (255, 165, 0), # LARANJA
    (255, 215, 0), # AMARELO OURO
    (46,213,115),  # VERDE ESMERALDA
    (55, 66, 250)  # AZUL ROYAL

]

# MEDIDAS DOS ELEMENTOS
BARRA_LARGURA = 120
BARRA_ALTURA = 16
BOLA_TAMANHO = 16

# MEDIDAS DAS GRLHAS DE BLOCOS
BLOCO_LINHAS = 5
BLOCO_COLUNAS = 10
BLOCO_ALTURA = 25
BLOCO_ESPACO = 6
MARGEM_TOPO = 55 # O ESPAÇO ESTA MAIOR PARA CABER O PLACAR
MARGEM_LATERAL = 30

def calcular_shake(tempo_shake,forca):
    """ Devolve um pequeno desvio aleatório (x, y) se o trmor estiver ativo. """
    if tempo_shake > 0:
        return random.randint(- forca, forca), random.randint(-forca,forca)
    return 0, 0


#DESENHO DO CENARIO
def desenhar_cenario(tela, offset=(0,0)):
    """Pinta o fundo e coloca uma moldura decorativana tela ."""
    tela.fill(COR_FUNDO)
    ox, oy = offset
    pygame.draw.rect(tela, COR_BORDA, (ox, oy, LARGURA, ALTURA), 4) # DESENHA UMA BORDA FINA AO REDOR DO ECRÃ

#DESENHO DA BARRA
def desenhar_barra(tela, barra_rect, offset=(0,0)):
    """Desenha a barra do jogador com os campos arrendondados."""
    ox, oy = offset
    rect_tremido = barra_rect.move(ox,oy)
    pygame.draw.rect(tela, COR_BARRA, rect_tremido, border_radius=8)

#DESENHO  DA BOLA
def desenhar_bola(tela, bola_rect, offset = (0,0)):
    """ Desenha a bola redonda redonda dentro do retangulo lógico """
    ox,oy = offset
    rect_tremido = bola_rect.move(ox,oy)
    pygame.draw.ellipse( tela, COR_BOLA, rect_tremido)

#DESENHO DOS BLOCOS
def desenhar_blocos(tela, lista_blocos, offset = (0,0)):
    ox, oy = offset
    for bloco_rect, cor in lista_blocos:
        rect_tremido = bloco_rect.move(ox,oy)
        pygame.draw.rect(tela, cor, rect_tremido, border_radius= 4)

#DESENHA O PLACAR
def desenhar_hud(tela,pontos, vidas):
    """ desenha a pontuação e as vidas restantes no topo do ecrâ. """
    fonte = pygame.font.SysFont("arial", 22, bold = True)

    texto_pontos = fonte.render(f"Pontos: {pontos}", True, COR_TEXTO)
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, COR_TEXTO)

    tela.blit(texto_pontos, (30,15))
    tela.blit(texto_vidas, (LARGURA - 120, 15))


def desenhar_fim_de_jogo(tela, venceu):
    """ Mostra no ecrã de vitória ou game over no centro da janela. """
    fonte_grande = pygame.font.SysFont("Arial", 48, bold = True)  
    fonte_pequena = pygame.font.SysFont("Arial", 22)

    if venceu:
        titulo = fonte_grande.render("PARABÉNS ! VOCÊ VENCEU!", True, COR_VITORIA) 

    else:
        titulo = fonte_grande.render("💥 GAME OVER! 💥", True, COR_DERROTA)   

    subtitulo = fonte_pequena.render("Pressione ESPAÇO para jogar novamente", True, COR_TEXTO)  

    #CENTRALIZAR OS TEXTOS MATEMATICAMENTE
    react_titulo = titulo.get_rect(center=(LARGURA // 2, ALTURA // 2-20))   
    rect_sub = subtitulo.get_rect(center=(LARGURA //2, ALTURA // 2 + 30))

    tela.blit(titulo, react_titulo)
    tela.blit(subtitulo, rect_sub)
