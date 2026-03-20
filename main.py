import pygame

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Obstaculo Demo")

inicio = True

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False

    tela.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()