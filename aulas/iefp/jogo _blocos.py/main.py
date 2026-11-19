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
    jogo = EstadoDoJogo()

    #LOOP PRINCIPAL
    while jogo.rodando:
        #LÓGICA
        jogo.processar_eventos()
        jogo.atualizar()

        # Design
        offset = design.calcular_shake(jogo.tempo_shake, jogo.forca_shake)
        design.desenhar_cenario(tela, offset)
        design.desenhar_barra(tela, jogo.barra, offset)
        design.desenhar_bola(tela, jogo.bola, offset)
        design.desenhar_blocos(tela, jogo.blocos, offset)
        design.desenhar_hud(tela, jogo.pontos, jogo.vidas)

        if jogo.jogo_terminado:
            design.desenhar_fim_de_jogo(tela, jogo.venceu)

        # Atualizar o ecra a 60 FPS 
        pygame.display.flip()
        relogio.tick(60)
    pygame.quit()
    sys.exit()

if __name__ == "__main__": # O main é uma porta de segurança para que execute o ficheiro paenas quando chamar o main.py
    iniciar_jogo()        

