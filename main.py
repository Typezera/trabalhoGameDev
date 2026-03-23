import pygame
import time
from obstaculo import Obstaculo
from player import Player
from game_over import tela_game_over, verificar_restart, sair_jogo
from score import salvar_recorde, carregar_recorde

pygame.init()

#configurações de tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Obstaculo Demo")

obstaculos = []

inicio = True

###Som de dano
som_dano = pygame.mixer.Sound("msc/hit01.wav")
som_dano.set_volume(0.5)


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


#ajuste para spawn
reaparecer = 0
player = Player()


tempo_final = 0

while inicio:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            inicio = False

    if game_over:
        tela_game_over(tela, fonte, tempo_final)

        if verificar_restart():
            player = Player()
            obstaculos = []
            tempo_final = 0
            tempo_inicio = time.time()
            game_over = False
        
        if sair_jogo():
            inicio = False
        
        continue



    tela.blit(background, (0,0))

    tempo_atual = time.time()
    tempo_vivo = time.time() - tempo_inicio
    dificuldade = int(tempo_vivo / 10) ## a cada 50s aumenta a dificuldade
    spawn = max(0.2, 0.6 - (tempo_vivo * 0.01))

    if tempo_atual - reaparecer > spawn:
        obstaculos.append(Obstaculo(dificuldade))
        reaparecer = tempo_atual

    obstaculos = [obs for obs in obstaculos if obs.y < altura]

    for obs in obstaculos:
        obs.mover()
        obs.desenhar(tela)
    

    for obs in obstaculos[:]:
        if player.colisao_player().colliderect(obs.colisao_obstaculo()):
            player.tomar_dano()
            som_dano.play()
            obstaculos.remove(obs)

        if player.hp <= 0:
            tempo_final = int(time.time() - tempo_inicio)
            salvar_recorde(tempo_final)
            game_over = True
    
    player.atualizar_dano()
    player.mover()
    player.desenhar(tela)

    ####tempo
    tempo_vivo = int(time.time() - tempo_inicio)

    #######Hud
    hp = fonte.render(f"HP: {player.hp}", True, (255, 255, 255))
    tempo = fonte.render(f"Tempo: {tempo_vivo}s", True, (255, 255, 0))
    recorde = carregar_recorde()
    texto_recorde = fonte.render(f"Recorde: {recorde}s", True, (255, 255, 255))
    tela.blit(texto_recorde, (10, 90))

    tela.blit(hp, (10, 10))
    tela.blit(tempo, (10, 50))

    pygame.display.flip()

pygame.quit()