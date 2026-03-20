import pygame
import random

class Obstaculo:
    def __init__(self):
        self.largura = 50
        self.altura = 50
        self.x = random.randint(0,750)
        self.y = 0
        self.velocidade = 1

    def mover(self):
        self.y += self.velocidade

    def restart(self):
        self.y = 0
        self.x = random.randint(0, 750)
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, (255, 0, 0), (self.x, self.y, self.largura, self.altura))