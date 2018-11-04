import pygame

titulo = "Carrera de la Cucaracha"
largura = 800
altura = 600
branco = (255,255,255)

pygame.display.set_caption(titulo)
fundo = pygame.image.load('img/fundo.png')
tela = pygame.display.set_mode((largura, altura), 0, 32)
pygame.mixer.music.load('Sons/La-Cucaracha.mp3')
pygame.mixer.music.play(-1)

tela.blit(fundo, (9, 4))



def TelaInicial():
    pygame.mixer.music.play(-1)
    while True:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 1
def Menu():

    tela.fill(branco)
    fundo = pygame.image.load('img/quarto.PNG')
    tela.blit(fundo, (0, 0))

    while True:

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer_music.stop()
                    return 2