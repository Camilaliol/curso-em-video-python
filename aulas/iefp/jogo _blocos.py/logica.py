import pygame 

class EstadoDoJogo:
    def _init_(self):
        self.rodando = True

    def processar_eventos(self):
        #local onde verificamos os comandos do sistema
        for eventos in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False    

    def atualizar(self):
        pass            