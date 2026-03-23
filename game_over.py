import pygame

def tela_game_over(tela, fonte, tempo_final):
    tela.fill((0,0,0))

    largura = tela.get_width()
    altura = tela.get_height()

    texto1 = fonte.render("GAME OVER", True, (255, 0, 0))
    texto2 = fonte.render(f"Tempo sobrevivido: {tempo_final}s", True, (255, 255, 0))
    texto3 = fonte.render("Pressione R para reiniciar", True, (255,255,255))
    texto4 = fonte.render("Pressione Q para sair do jogo!", True, (255, 255, 255))

    rect1 = texto1.get_rect(center=(largura // 2, altura // 2 - 60))
    rect2 = texto2.get_rect(center=(largura // 2, altura // 2))
    rect3 = texto3.get_rect(center=(largura // 2, altura // 2 + 50))
    rect4 = texto4.get_rect(center=(largura // 2, altura // 2 + 100))

    tela.blit(texto1, rect1)
    tela.blit(texto2, rect2)
    tela.blit(texto3, rect3)
    tela.blit(texto4, rect4)

    pygame.display.flip()

def verificar_restart():
    teclas= pygame.key.get_pressed()
    return teclas[pygame.K_r]

def sair_jogo():
    teclas= pygame.key.get_pressed()
    return teclas[pygame.K_q]