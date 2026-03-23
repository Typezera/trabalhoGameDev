import pygame
import time

class Player:
    def __init__(self):
        self.x = 350
        self.y = 500
        self.largura = 50
        self.altura = 50
        self.velocidade = 2.5
        self.hp = 3
        self.dano = False
        self.tempo_dano = 0

    def mover (self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade

        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidade

        if self.x < 0:
            self.x = 0
        
        if self.x > 800 - self.largura:
            self.x = 800 - self.largura
    

    def tomar_dano(self):
        if not self.dano:
            self.hp -= 1
            self.dano = True
            self.tempo_dano = time.time()

    def atualizar_dano(self):
        if self.dano:
            if time.time() - self.tempo_dano > 0.3:
                self.dano = False

    def colisao_player(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)


    def desenhar(self, tela):
        cor = (0, 255, 0)

        if self.dano:
            if int(time.time() * 10) % 2 == 0:
                cor = (255, 0, 0)

        pygame.draw.rect(tela, cor, (self.x, self.y, self.largura, self.altura))