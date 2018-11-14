import pygame

titulo = "Carrera de la Cucaracha"
telaLargura = 1024
telaAltura = 768
branco = (255,255,255)

pygame.init()

pygame.display.set_caption(titulo)
tela = pygame.display.set_mode((telaLargura, telaAltura), 0, 32)
pygame.mixer.music.load('Sons/La-Cucaracha.mp3')
fundo = pygame.image.load('img/fundo.png')


def ajustaimagem(img):
    global largura, altura, fundo
    fundo = pygame.image.load(img)
    fundo = pygame.transform.scale(fundo, (telaLargura, telaAltura))

def TelaInicial():
    global fundo
    pygame.mixer.music.play(-1)
    ajustaimagem('img/fundo.png')

    while True:

        pygame.display.update()
        tela.blit(fundo, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 1
def Menu():
    global fundo
    pygame.mixer.music.play(-1)
    ajustaimagem('img/quarto.PNG')

    while True:
        tela.blit(fundo, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pygame.mixer_music.stop()
                    return 2
                if event.key == pygame.K_2:
                    return 4
def Loja():

    global fundo
    ajustaimagem('img/loja.png')

    while True:
        tela.blit(fundo, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 1