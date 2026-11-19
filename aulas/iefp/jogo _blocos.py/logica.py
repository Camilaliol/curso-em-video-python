import pygame 
import design

class EstadoDoJogo:
    def __init__(self):
        self.rodando = True
        self.reiniciar()

    def reiniciar(self):
        self.pontos = 0
        self.vidas = 3
        self.jogo_terminado = False
        self.venceu = False
        self.tempo_shake = 0 # Guarda o contado
        self.combo = 0
        self.forca_shake = 0
        self.velocidade_base = 5
        self.bola_vel_x = self.velocidade_base
        self.bola_vel_y = -self.velocidade_base

        #   CONFIGURANDO A BARRA:
        pos_x = (design.LARGURA // 2) - (design.BARRA_LARGURA // 2)
        pos_y = design.ALTURA - 45
        self.barra = pygame.Rect(pos_x, pos_y, design.BARRA_LARGURA, design.BARRA_ALTURA)
        self.barra_velocidade = 8

        #CONFIGURAÇÃO DA BOLA - INICIANDO NO CENTRO
        self.bola = pygame.Rect(
            design.LARGURA //2,
            design.ALTURA // 2,
            design.BOLA_TAMANHO,
            design.BOLA_TAMANHO
        )
        self.bola_vel_x = 5
        self.bola_vel_y = -5 # o NEGATIVO FAZ COM QUE A BOLA SUBA PRIMEIRO    
        self.blocos = []
        self.criar_blocos()

    def criar_blocos(self):
        """ gera a grelha de blocos com base nas medidas do design.py """  
        espaco_util = design.LARGURA - ( design.MARGEM_LATERAL * 2) 
        bloco_largura = (espaco_util - (design.BLOCO_COLUNAS - 1) * design.BLOCO_ESPACO) // design.BLOCO_COLUNAS

        for linha in range(design.BLOCO_LINHAS):
            cor_atual = design.CORES_BLOCOS[linha % len(design.CORES_BLOCOS)]
            for coluna in range(design.BLOCO_COLUNAS):
                x = design.MARGEM_LATERAL + coluna * (bloco_largura + design.BLOCO_ESPACO)
                y = design.MARGEM_TOPO + linha * (design.BLOCO_ALTURA + design.BLOCO_ESPACO)

                retangulo = pygame.Rect(x,y, bloco_largura, design.BLOCO_ALTURA)
                self.blocos.append((retangulo,cor_atual))

    def processar_eventos(self):
        #local onde verificamos os comandos do sistema
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False   

            # reiniciando ao pressionar ESPAÇO após o fim do jogo
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and self.jogo_terminado:
                    self.reiniciar()     

    def atualizar(self):

        #Congela o jogo se ja tive terminado
        if self.jogo_terminado:
            return
        if self.tempo_shake > 0:
            self.tempo_shake -= 1

        # MOVIMENTO DA BARRA
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT] and self.barra.left > 4:
            self.barra.x -= self.barra_velocidade

        if teclas[pygame.K_RIGHT] and self.barra.right < design.LARGURA -4: 
            self.barra.x += self.barra_velocidade

        #MOVIMENTO DA BOLA
        self.bola.x += self.bola_vel_x
        self.bola.y += self.bola_vel_y   

    # COLISÃO COM  AS PAREDES 
            # PAREDE ESQUERDA OU DI8REITA: INVERTE A DIREÇÃO HORIZONTAL
        if self.bola.left <= 4 or self.bola.right >= design.LARGURA -4:
            self.bola_vel_x *= -1

            #TETO: INVERSÃO DA DIREÇÃO VERTICAL
        if self.bola.top <= 4:
            self.bola_vel_y *= -1

            #CHÃO ( NESTE MOMENTO SE A BOLA CAIXA EMBAIXO ELA VOLTA AO CENTRO)     
        if self.bola.bottom >= design.ALTURA:
            self.vidas -= 1
            if self.vidas <=0:
                self.jogo_terminado = True
                self.venceu = False

            else:
                self.bola.center = (design.LARGURA //2, design.ALTURA // 2)
                self.bola_vel_y = -5     

    #COLISÃO DA BOLA COM A BARRA            
        #SÓ REBATE SE A BOLA ESTIVER A DESCER
        if self.bola.colliderect(self.barra) and self.bola_vel_y > 0:
            self.bola_vel_y *= -1
            self.combo = 0
            if self.bola_vel_x > 0:
                self.bola_vel_x = self.velocidade_base
            else:
                self.bola_vel_x = -self.velocidade_base    

        #COLISÃO DA BOLA COM OS BLOCOS
        for item in self.blocos[:]:
            bloco_rect, com = item
            if self.bola.colliderect(bloco_rect):
                self.bola_vel_y *= -1
                self.blocos.remove(item)
                self.pontos += 10
                self.combo += 1
                self.tempo_shake = 8 #ativa o tremor
                #COEMÇA EM 3 PÍXEIS E SOBE +2 POR CADA BLOCO SEGUIDO (o 12 é o limite maximo)
                self.forca_shake = min(3 + (self.combo *2), 12)

                #ACELERA A BOLA SE QUEBRAR MAIS DE UM BLOCO
                if self.combo > 1:
                    nova_vel = min(self.velocidade_base + (self.combo - 1), 10)

                    if self.bola_vel_x > 0:
                        self.bola_vel_x = nova_vel
                    else:   
                        self.bola_vel_x = -nova_vel 

                    if self.bola_vel_y >0:
                        self.bola_vel_y = nova_vel
                    else:
                        self.bola_vel_y = -nova_vel        

                break

        if len(self.blocos) == 0:
                self.jogo_terminado = True
                self.venceu = True        