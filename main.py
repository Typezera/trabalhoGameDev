import pygame
import time
from obstaculo import Obstaculo
from player import Player

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Obstaculo Demo")


reaparecer = 0
spawn = 0.6
obstaculos = []
player = Player()

inicio = True

pygame.mixer.music.load("msc/ObservingTheStar.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

background = pygame.image.load("background/vortex.png") #grid_bg.png  vortex.png
background = pygame.transform.scale(background, (largura,altura))

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False

    tela.blit(background, (0,0))

    tempo_atual = time.time()

    if tempo_atual - reaparecer > spawn:
        obstaculos.append(Obstaculo())
        reaparecer = tempo_atual

    obstaculos = [obs for obs in obstaculos if obs.y < altura]

    for obs in obstaculos:
        obs.mover()
        obs.desenhar(tela)

    player.mover()
    player.desenhar(tela)

    pygame.display.flip()

pygame.quit()