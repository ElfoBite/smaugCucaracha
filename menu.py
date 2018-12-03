import pygame
from jogo import personagem
from exercicios import QualExercico

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
                if event.key == pygame.K_0:
                    return 6

def Loja():
    global fundo
    exercicio = QualExercico()
    font = pygame.font.Font('fontes/UbuntuMono-Bold.ttf', 25)
    ajustaimagem('img/loja.png')
    resposta = 0
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    while True:
        if personagem.ponto > 30:
            if resposta == 0:
                tela.fill(preto)
                imgpontos = font.render("Pontos:"+str(personagem.ponto), True, branco)
                tela.blit(imgpontos, (20, 0))
                imgPergunta = font.render(exercicio['pergunta1'], True, branco)
                tela.blit(imgPergunta, (20, 40))
                imgPergunta2 = font.render(exercicio['pergunta2'], True, branco)
                tela.blit(imgPergunta2, (20, 60))
                resposta1 = font.render('1.'+exercicio['1']['texto'], True, branco)
                tela.blit(resposta1, (20, 100))
                resposta2 = font.render('2.'+exercicio['2']['texto'], True, branco)
                tela.blit(resposta2, (20, 120))
                resposta3 = font.render('3.'+exercicio['3']['texto'], True, branco)
                tela.blit(resposta3, (20, 140))
                resposta4 = font.render('4.'+exercicio['4']['texto'], True, branco)
                tela.blit(resposta4, (20, 160))
                resposta5 = font.render('5.'+exercicio['5']['texto'], True, branco)
                tela.blit(resposta5, (20, 180))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return 6
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            resposta = exercicio['1']['?']
                        elif event.key == pygame.K_2:
                            resposta = exercicio['2']['?']
                        elif event.key == pygame.K_3:
                            resposta = exercicio['3']['?']
                        elif event.key == pygame.K_4:
                            resposta = exercicio['4']['?']
                        elif event.key == pygame.K_5:
                            resposta = exercicio['5']['?']
                        if event.key == pygame.K_ESCAPE:
                           return 1

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
