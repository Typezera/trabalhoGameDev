import pygame
import random

class Obstaculo:
    def __init__(self):
        self.largura = random.randint(30, 100)
        self.altura = random.randint(30, 100)
        self.x = random.randint(0, 800 - self.largura)
        self.y = 0
        self.velocidade = 0.3

    def mover(self):
        self.y += self.velocidade

    def restart(self):
        self.y = 0
        self.x = random.randint(0, 750)
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, (255, 0, 0), (self.x, self.y, self.largura, self.altura))