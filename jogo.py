import pygame
import random
from personagem import Personagem


teste = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1]]

maca = pygame.image.load('img/maca.jpg')
maca = pygame.transform.scale(maca, (40, 40))
s = 0

def MudaMaca():
    global s
    s = 0
    y = 0
    for i in teste:
        x = 0
        for j in i:
            if j == 2:
                teste[y][x] = 0
            x += 1
        y += 1

    sair = True

    while sair:
        yMaca = random.randint(0,23)
        xMaca = random.randint(0,31)
        if teste[yMaca][xMaca] == 0:
            teste[yMaca][xMaca] = 2
            sair = False

def Jogar():
    global s
    branco = (255, 255, 255)
    preto = (0, 0, 0)

    telaLargura = 1024
    telaAltura = 768

    personagem = Personagem(telaLargura, telaAltura)

    fps = pygame.time.Clock()
    tela = pygame.display.set_mode((telaLargura,telaAltura),pygame.DOUBLEBUF,32)
    fundo = pygame.image.load('Cenarios/fase1.png')
    fundo = pygame.transform.scale(fundo, (telaLargura, telaAltura))
    s = 600


    while True:

        s += 1
        segundo = s/60

        tela.blit(fundo, (0, 0))

        if segundo >= 10:
            MudaMaca()

        x, y = 0, 0
        muros = []
        macaRect = pygame.Rect(0, 0, 0, 0)

        for i in teste:
            x = 0
            for j in i:
                if j == 1:
                    muros.append(pygame.Rect(x, y, (telaAltura / teste.__len__()), (telaLargura / i.__len__())))

                if j == 2:

                    macaRect = pygame.Rect(x, y, 40, 40)
                    tela.blit(maca, (x, y))

                x += telaAltura / teste.__len__()
            y += telaLargura / i.__len__()

        tela.blit(personagem.ativo, (personagem.x, personagem.y))
        personagem.x += personagem.moveX
        personagem.y += personagem.moveY
        personagem.TestaLimiteDaTela(telaLargura, telaAltura)
        personagem.TestaMuro(muros)
        pegou = personagem.TestaMaca(macaRect)
        if pegou == 1:
            MudaMaca()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 6
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    personagem.AndaEsquerda()
                if event.key == pygame.K_RIGHT:
                    personagem.AndaDireita()
                if event.key == pygame.K_UP:
                    personagem.AndaCima()
                if event.key == pygame.K_DOWN:
                    personagem.AndaBaixo()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    personagem.ParaX()
                if event.key == pygame.K_RIGHT:
                    personagem.ParaX()
                if event.key == pygame.K_UP:
                    personagem.ParaY()
                if event.key == pygame.K_DOWN:
                    personagem.ParaY()
        fps.tick(60)
        pygame.display.update()