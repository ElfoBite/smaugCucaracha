#daniel da costa ruy
#inicio projeto menu a modo daniel
#pratica de python/estudo para programação e evolução na minha carreira.
#Projeto Smaug Fatec 2018-carapicuiba- 2ºciclo.
#===============================================================================#

#importação da biblioteca pygame
import pygame
import sys
import game


# iniciamos o modulo pygame
pygame.init()

try:
    # o nosso jogo
    meu_game = game.Game(title="Carreira de la cucaracha", fullscreen=False, width=800, height=600)

    # carregamos os recursos necessarios ao jogo
    meu_game.load_content()
    # Iniciamos o loop do jogo
    # Aqui vamos desenhar tudo e atualizar o nosso jogo
    while meu_game.running:
        # Obtemos os eventos SDL
        events = pygame.event.get()
        for event in events:
            # Se clicarmos no X para fechar a janela
            if event.type == pygame.QUIT:
                meu_game.running = False  # Finalizamos o loop
            # agora damos um update e um draw no nosso jogo
        meu_game.update()
        meu_game.draw()

# aqui vamos tratar das excecoes do nosso codigo
except Exception as ex:
    print(ex.message)


finally:

    # caso aconteca algum erro,
    # limpamos os recursos
    # e saimos do processo
    if meu_game:
        meu_game.unload_content()
    pygame.quit()

