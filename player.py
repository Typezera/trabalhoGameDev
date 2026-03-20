import pygame

class Player:
    def __init__(self):
        self.x = 350
        self.y = 500
        self.largura = 50
        self.altura = 50
        self.velocidade = 2

    def mover (self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade

        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidade

        if self.x < 0:
            self.x = 0
        
        if self.x > 800 - self.largura:
            self.x = 800 - self.altura
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, (0, 255, 0), (self.x, self.y, self.largura, self.altura))