import pygame
import sys
import design
from logica import EstadoDoJogo

def iniciar_jogo():
    pygame.init()
    tela = pygame.display.set_mode((design.LARGURA, design.ALTURA))
    pygame.display.set_caption(design.TITULO)
    relogio = pygame.time.Clock()

    #CRIAÇÃO DO CEREBRO DO JOGO
    jogo = EstadoDoJogo

    #LOOP PRINCIPAL
    while jogo.rodando:
        #LÓGICA
        jogo.processar_eventos()
        jogo.atualizar()

        # Design
        design.desenhar_cenario(tela)

        # Atualizar o ecra a 60 FPS 
        pygame.display.flip()
        relogio.tick(60)
    pygame.quit()
    sys.exit()

if _name_ == "_main_": # O main é uma porta de segurança para que execute o ficheiro paenas quando chamar o main.py
    iniciar_jogo()        

