import pygame
from obstaculo import Obstaculo
from player import Player

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Obstaculo Demo")

obstaculo = Obstaculo()
player = Player()

inicio = True

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False

    tela.fill((30, 30, 30))

    obstaculo.mover()
    obstaculo.desenhar(tela)

    if obstaculo.y > altura:
        obstaculo.restart()

    player.mover()
    player.desenhar(tela)

    pygame.display.flip()

pygame.quit()