import pygame
import random

class Obstaculo:
    def __init__(self, dificuldade):
        base = 30 + int(dificuldade * 2)
        self.largura = random.randint(base, base + 50)
        self.altura = random.randint(base, base + 50)
        self.x = random.randint(0, 800 - self.largura)
        self.y = 0
        self.velocidade = random.uniform(0.4, 0.8) + (dificuldade * 0.5)
        self.cores = [
            (255, 0, 0),     # vermelho
            (255, 255, 0),   # amarelo
            (0, 0, 255),     # azul
            (255, 255, 255)  # branco
        ]
        self.cor = random.choice(self.cores)

    def mover(self):
        self.y += self.velocidade

    def restart(self):
        self.y = 0
        self.x = random.randint(0, 750)
    

    def colisao_obstaculo(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))