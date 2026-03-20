import pygame
from player import Player

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Obstaculo Demo")

player = Player()

inicio = True

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False

    tela.fill((0, 0, 0))

    player.mover()
    player.desenhar(tela)

    pygame.display.flip()

pygame.quit()