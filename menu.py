import pygame
def MENU():
    titulo = "Carrera de la Cucaracha"
    largura = 800
    altura = 600
    Sair = True
    branco = (255,255,255)
    try:
        pygame.init()
    except:
        print("O modulo pygame não foi iniciado com sucesso")

    pygame.display.set_caption(titulo)
    fundo = pygame.image.load('img/fundo.png')
    tela = pygame.display.set_mode((largura, altura), 0, 32)

    pygame.mixer.music.load('Sons/La-Cucaracha.mp3')
    pygame.mixer.music.play(-1)

    tela.blit(fundo, (9, 4))

    while Sair:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    tela.fill(branco)
                    fundo = pygame.image.load('img/quarto.PNG')
                    tela.blit(fundo, (0, 0))
                if event.key == pygame.K_ESCAPE:
                    Sair = False

    pygame.quit()