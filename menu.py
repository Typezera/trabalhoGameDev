import pygame

def tela_menu(tela, fonte):
    tela.fill((0, 0, 0))

    largura = tela.get_width()
    altura = tela.get_height()

    titulo = fonte.render("JOGO DE DESVIO", True, (255, 255, 255))
    instrucoes1 = fonte.render("Use as setas <- -> para se mover", True, (200, 200, 200))
    instrucoes2 = fonte.render("Desvie dos obstáculos", True, (200, 200, 200))
    iniciar = fonte.render("Pressione ENTER para começar", True, (255, 255, 0))

    tela.blit(titulo, titulo.get_rect(center=(largura//2, altura//2 - 80)))
    tela.blit(instrucoes1, instrucoes1.get_rect(center=(largura//2, altura//2 - 20)))
    tela.blit(instrucoes2, instrucoes2.get_rect(center=(largura//2, altura//2 + 20)))
    tela.blit(iniciar, iniciar.get_rect(center=(largura//2, altura//2 + 80)))

    pygame.display.flip()
