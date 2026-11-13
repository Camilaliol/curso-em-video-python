import pygame 

#TAMANHO DA TELA
LARGURA = 800
ALTURA = 600
TITULO = "<<<<<<<<<<<<<<< BRICK BREAKER >>>>>>>>>>>>>>>>"

# PALETA DE CORES  
COR_FUNDO = (20,24,36)
COR_BORDA = (50,60,85)
COR_BARRA = ()

def desenhar_cenario(tela):
    "Pinta o fundo e coloca uma moldura decorativana tela ."""
    tela.fill(COR_FUNDO)
# DESENHA UMA BORDA FINA AO REDOR DO ECRÃ
    PYGAME.DRAW.RECT(TELA, COR_BORDA, (0, 0, LARGURA, ALTURA), 4)    