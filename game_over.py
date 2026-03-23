import pygame

def tela_game_over(tela, fonte):
    tela.fill((0,0,0))

    texto1 = fonte.render("GAME OVER", True, (255, 0, 0))
    texto2 = fonte.render("Pressione R para reiniciar", True, (255,255,255))
    texto3 = fonte.render("Pressione Q para sair do jogo!", True, (255, 255, 255))

    tela.blit(texto1, (300, 250))
    tela.blit(texto2, (200,300))
    tela.blit(texto3, (100,400))

    pygame.display.flip()

def verificar_restart():
    teclas= pygame.key.get_pressed()
    return teclas[pygame.K_r]

def sair_jogo():
    teclas= pygame.key.get_pressed()
    return teclas[pygame.K_q]