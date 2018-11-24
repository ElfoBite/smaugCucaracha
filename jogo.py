import pygame
from personagem import Personagem
from maca import Maca
from fase import abreFase
faseCaminho = 'Cenarios/fase'
Nfase = 1
telaLargura = 960
telaAltura = 690

tileX = int(telaLargura / 32)
tileY = int(telaAltura / 23)

muros = []
maca = Maca(tileX, tileY, 0)
macaPodre = Maca(tileX, tileY, 1)

personagem = Personagem(50, 50)

teste = abreFase(faseCaminho + str(personagem.fase))

fps = pygame.time.Clock()
tela = pygame.display.set_mode((telaLargura, telaAltura), pygame.DOUBLEBUF, 32)
font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 25)

def AtualizaMuros(fase):
    global muros, tileX, tileY, teste
    y = 0
    for i in fase:
        x = 0
        for j in i:
            if j == 1:
                muros.append(pygame.Rect(x, y, tileX, tileY))
            x += tileX
        y += tileY

def RenderisaPontos(pontos):
    texto = "Pontos: " + str(pontos)
    imgPontos = font.render(texto, True, (255, 255, 255))
    return imgPontos

def MudaFase(n):
    global teste, muros, personagem, maca, macaPodre
    personagem.x = 50
    personagem.y = 50
    personagem.Para()
    muros = []
    personagem.fase = n
    teste = abreFase(faseCaminho + str(personagem.fase))
    AtualizaMuros(teste)
    teste = maca.Muda(fase=teste, tileY=tileY, tileX=tileX)
    teste = macaPodre.Muda(fase=teste, tileY=tileY, tileX=tileX)

def Jogar():
    global s, tela, personagem, maca, macaPodre, teste, Nfase

    fundo = pygame.image.load('Cenarios/fase'+str(personagem.fase)+'.png')
    fundo = pygame.transform.scale(fundo, (telaLargura, telaAltura))
    AtualizaMuros(teste)
    s = 600
    tick = 0

    while True:
        tick += 1
        maca.tick += 1
        maca.segundo = maca.tick/60
        macaPodre.tick += 1
        macaPodre.segundo = macaPodre.tick/60

        personagem.x += personagem.moveX
        personagem.y += personagem.moveY
        personagem.TestaLimiteDaTela(telaLargura, telaAltura)
        personagem.TestaMuro(muros)

        if tick >= 60:
            personagem.ponto -= 1
            tick = 0

        if personagem.TestaMaca(maca.rect):
            teste = maca.Muda(fase=teste, tileY=tileY, tileX=tileX)

        if personagem.TestaMacaPodre(macaPodre.rect):
            teste = macaPodre.Muda(fase=teste, tileY=tileY, tileX=tileX)

        if maca.segundo >= 5:
           teste = maca.Muda(fase=teste, tileY=tileY, tileX=tileX)

        if macaPodre.segundo >= 5:
           teste = macaPodre.Muda(fase=teste, tileY=tileY, tileX=tileX)

        if personagem.ponto < 0:
            return 7

        if personagem.ponto >= 100 and personagem.fase == 1:
            MudaFase(2)
            return 1

        tela.blit(fundo, (0, 0))
        tela.blit(maca.img, (maca.x, maca.y))
        tela.blit(macaPodre.img, (macaPodre.x, macaPodre.y))
        tela.blit(personagem.ativo, (personagem.x, personagem.y))
        tela.blit(RenderisaPontos(personagem.ponto), (0, 0))

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
                if event.key == pygame.K_ESCAPE:
                    return 1

        pygame.display.update()

        fps.tick(60)

def GameOver():
    global Nfase, personagem
    fontGameOver = pygame.font.Font('img/TlwgTypist-Bold.ttf', 90)
    font = pygame.font.Font('img/TlwgTypist-Bold.ttf', 30)
    gameOvertxt = fontGameOver.render("GAME OVER", True, (0, 0, 0))
    gameOverContinueTxt = font.render("Aperte ESC para iniciar um novo jogo", True, (0, 0, 0))
    tela.blit(gameOvertxt, (250, 200))
    tela.blit(gameOverContinueTxt, (170, 400))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 6
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    MudaFase(1)
                    personagem = Personagem(50, 50)
                    return 1
