import pygame
import time
from obstaculo import Obstaculo
from player import Player
from game_over import tela_game_over, verificar_restart, sair_jogo

pygame.init()

#configurações de tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Obstaculo Demo")

#ajuste para spawn
reaparecer = 0
spawn = 0.6
obstaculos = []
player = Player()

inicio = True

#mixer para musica
pygame.mixer.music.load("msc/ObservingTheStar.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#imagem de fundo
background = pygame.image.load("background/vortex.png") #grid_bg.png  vortex.png
background = pygame.transform.scale(background, (largura,altura))


# hud
fonte = pygame.font.SysFont(None, 36)

####tempo de inicio do jogo para o score
tempo_inicio = time.time()

#######Game Over
game_over = False

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
    

    for obs in obstaculos[:]:
        if player.colisao_player().colliderect(obs.colisao_obstaculo()):
            player.tomar_dano()
            obstaculos.remove(obs)

        if player.hp <= 0:
            game_over = True


    if game_over:
        tela_game_over(tela, fonte)

        if verificar_restart():
            player = Player()
            obstaculos = []
            tempo_inicio = time.time()
            game_over = False
        
        if sair_jogo():
            inicio = False
        
        continue
    
    player.atualizar_dano()
    player.mover()
    player.desenhar(tela)

    ####tempo
    tempo_vivo = int(time.time() - tempo_inicio)

    #######Hud
    hp = fonte.render(f"HP: {player.hp}", True, (255, 255, 255))
    tempo = fonte.render(f"Tempo: {tempo_vivo}s", True, (255, 255, 0))

    tela.blit(hp, (10, 10))
    tela.blit(tempo, (10, 50))

    pygame.display.flip()

pygame.quit()