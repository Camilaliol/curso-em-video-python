import pygame
import time
from pathlib import Path

pygame.init()
pygame.mixer.init()

caminho_projeto = Path(__file__).resolve().parents[1]
caminho_musica = caminho_projeto / "let_me_be.mp3"

pygame.mixer.music.load(str(caminho_musica))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

try:
    while pygame.mixer.music.get_busy():
        time.sleep(1) 
except KeyboardInterrupt:
    print("\nReprodução interrompida pelo utilizador.")

pygame.mixer.music.stop()
pygame.quit()