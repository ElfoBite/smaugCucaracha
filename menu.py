import pygame
from jogo import personagem

titulo = "Carrera de la Cucaracha"
telaLargura = 1024
telaAltura = 768
branco = (255, 255, 255)

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
    font = pygame.font.Font('fontes/TlwgTypist-Bold.ttf', 30)
    continuar = font.render("Aperte ENTER", True, (0, 0, 0))

    while True:
        tela.blit(fundo, (0, 0))
        tela.blit(continuar, (500, 500))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 6
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return 1
        pygame.display.update()

def Menu():
    global fundo
    pygame.mixer.music.play(-1)
    ajustaimagem('img/quarto.PNG')

    while True:
        tela.blit(fundo, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 6
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 2
                if event.key == pygame.K_2:
                    return 4

def Loja():
    global fundo
    font = pygame.font.Font('fontes/TlwgTypist-Bold.ttf', 25)
    ajustaimagem('img/loja.png')
    resposta = 0
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    while True:
        if personagem.ponto > 30:
            if resposta == 0:
                tela.fill(preto)
                imgpontos = font.render("Pontos:"+str(personagem.ponto), True, branco)
                imgPergunta = font.render("Dado os Pontos (2, 3) e (4, 5) qual a equação da reta?", True, branco)
                resposta1 = font.render("1. y = x+2", True, branco)
                resposta2 = font.render("2. y = x+1", True, branco)
                resposta3 = font.render("3. y = x", True, branco)
                resposta4 = font.render("4. y = 2x+1", True, branco)
                resposta5 = font.render("5. y = x+5", True, branco)
                tela.blit(imgpontos, (20, 20))
                tela.blit(imgPergunta, (20, 40))
                tela.blit(resposta1, (20, 80))
                tela.blit(resposta2, (20, 100))
                tela.blit(resposta3, (20, 120))
                tela.blit(resposta4, (20, 140))
                tela.blit(resposta5, (20, 160))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            resposta = 2
                        elif event.key == pygame.K_2:
                            resposta = 1
                        elif event.key == pygame.K_3:
                            resposta = 2
                        elif event.key == pygame.K_4:
                            resposta = 2
                        elif event.key == pygame.K_5:
                            resposta = 2
            elif resposta == 2:
                personagem.ponto -= 30
                resposta = 0
            else:
                tela.blit(fundo, (0, 0))
        else:
            imgErro = font.render("Você não possui pontos suficiente para entrar na loja", True, branco)
            tela.fill(preto)
            tela.blit(imgErro, (20, 20))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 6
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 1
