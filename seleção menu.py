import pygame

pg = pygame
titulo = "Carrera de la Cucaracha"
telaLargura = 1024
telaAltura = 768
branco = (255,255,255)
blocopermanente = True
selecao = True

pygame.init()

pygame.display.set_caption(titulo)
tela = pygame.display.set_mode((telaLargura, telaAltura), 0, 32)
pygame.mixer.music.load('Sons/La-Cucaracha.mp3')
# = pygame.image.load('img/fundo.png')

def fixo ():

        font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 30)
        fixo = font.render(">", True, (0, 0, 0))
        tela.blit(fixo, ((largura/2)+200, (altura/2)+35))

def menu_selecao ():

        if menu_selecao == 1:
            tela.fill((255, 255, 255))
            font = pygame.font.Font ('img/TlwgTypist-Bold.ttf', 30)
            iniciar = font.render("INICIAR", True (0, 0, 0))
            tela.blit(iniciar,((largura/2)+215, (altura/2)+35))

            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 20)
            configuracoes = font.render("CONFIGURAÇÕES", True(60, 60, 60))
            tela.blit(configuracoes, ((largura / 2) + 215, (altura / 2) + 75))


            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 20)
            loja = font.render("LOJA", True(60, 60, 60))
            tela.blit(loja, ((largura / 2) + 215, (altura / 2) + 105))


            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 20)
            sair = font.render("SAIR", True, (60, 60, 60))
            tela.blit ( sair, (largura / 2) + 215, (altura / 2) + 135 )

        if menu_selecao == 2:
            tela.fill((255, 255, 255))
            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 20)
            iniciar = font.render("INICIAR", True, (60, 60, 60))
            tela.blit(iniciar, ((largura / 2) + 215, (altura / 2) + 5))

            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 30)
            configuracoes = font.render ( "CONFIGURAÇÕES", True, (0, 0, 0) )
            tela.blit(configuracoes, ((largura / 2) + 215, (altura / 2) + 35))

            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 20)
            loja = font.render("lOJA", True, (60, 60, 60))
            tela.blit(loja, ((largura / 2) + 215, (altura / 2) + 75))

            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 20)
            sair = font.render("SAIR", True, (60, 60, 60))
            tela.blit(sair, ((largura / 2) + 215, (altura / 2) + 105

        if menu_selecao == 3:
            tela.fill((255, 255, 255))
            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 20)
            iniciar = font.render("INICIAR", True, (60, 60, 60))
            tela.blit(iniciar, ((largura / 2) + 215, (altura / 2)-25))

            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 30)
            configuracoes = font.render("CONFIGURAÇÕES", True, (0, 0 0))
            tela.blit(configuracoes, ((largura / 2) + 215, (altura / 2) + +5))

            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 30)
            loja = font.render("lOJA", True, (60, 60, 60))
            tela.blit(loja, ((largura / 2) + 215, (altura / 2) + 35))

            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 20)
            sair = font.render("SAIR", True, (60, 60, 60))
            tela.blit(sair, ((largura / 2) + 215, (altura / 2) + 75))

        if menu_selecao == 4:
            tela.fill((255, 255, 255))
            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 20)
            iniciar = font.render("INICIAR", True, (60, 60, 60))
            tela.blit(iniciar, ((largura / 2) + 215, (altura / 2) - 55))

            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 30)
            configuracoes = font.render("CONFIGURAÇÕES", True, (0, 0 0))
            tela.blit(configuracoes, ((largura / 2) + 215, (altura / 2) + -25))

            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 20)
            loja = font.render("lOJA", True, (60, 60, 60))
            tela.blit(loja, ((largura / 2) + 215, (altura / 2) + 5))

            font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 30)
            sair = font.render("SAIR", True, (60, 60, 60))
            tela.blit(sair, ((largura / 2) + 215, (altura / 2) + 35))

    if menu_selecao >= 5:
        menu_selecao = 4
    if menu_selecao <= 0:
        menu_selecao = 1

while True
    selecao()
    fixo()
    tela.blit(tela, (0, 0))
    pygame.display.update()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if (event.type == KEY_DOWN):
            menu_selecao = menu_selecao + 1
            if (event.key == K_DOWN):
                menu_selecao = menu_selecao - 1

    print(menu_selecao)


