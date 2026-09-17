import pygame  # importa a biblioteca Pygame para som e multimídia
import time  # importa o módulo time para pausar o loop
from pathlib import Path  # importa Path para manipular caminhos de arquivos

pygame.init()  # inicializa todos os módulos do Pygame
pygame.mixer.init()  # inicializa o mixer de áudio do Pygame

caminho_projeto = (
    Path(__file__).resolve().parents[1]
)  # obtém o caminho da pasta do projeto
caminho_musica = (
    caminho_projeto / "let_me_be.mp3"
)  # cria o caminho completo até o arquivo de música

pygame.mixer.music.load(str(caminho_musica))  # carrega a música para reprodução
pygame.mixer.music.set_volume(0.5)  # define o volume para 50%
pygame.mixer.music.play(-1)  # inicia a música em loop infinito (-1)

try:
    while pygame.mixer.music.get_busy():  # enquanto a música estiver tocando
        time.sleep(1)  # espera 1 segundo antes de verificar novamente
except KeyboardInterrupt:
    print(
        "\nReprodução interrompida pelo utilizador."
    )  # mensagem se o usuário interromper com Ctrl+C

pygame.mixer.music.stop()  # para a reprodução da música
pygame.quit()  # finaliza o Pygame e libera recursos
