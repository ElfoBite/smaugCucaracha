import pygame
from personagem import Personagem
from maca import Maca
from fase import abreFase
faseCaminho = 'Cenarios/fase'
Nfase = 1
telaLargura = 1024
telaAltura = 768
preto = (255, 255, 255)

tileX = int(telaLargura / 32)
tileY = int(telaAltura / 23)

muros = []
maca = Maca(tileX, tileY, 0)
macaPodre = Maca(tileX, tileY, 1)

personagem = Personagem(50, 50)

teste = abreFase(personagem.fase)

fps = pygame.time.Clock()
tela = pygame.display.set_mode((telaLargura, telaAltura), pygame.DOUBLEBUF, 32)

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
    font = pygame.font.Font('fontes/TlwgTypist-Bold.ttf', 25)
    texto = "Pontos: " + str(pontos)
    imgPontos = font.render(texto, True, preto)
    return imgPontos

def MudaFase(n):
    global teste, muros, personagem, maca, macaPodre,fundo
    font = pygame.font.Font('fontes/TlwgTypist-Bold.ttf', 25)
    nomeFase = ('1. Sala', '2. Cozinha', '3. Banheiro', '4. Escritorio', '5. Jardim')
    personagem.x = 50
    personagem.y = 50
    personagem.Para()
    muros = []
    personagem.fase = n
    fundo = pygame.image.load('Cenarios/fase'+str(personagem.fase)+'.png')
    fundo = pygame.transform.scale(fundo, (telaLargura, telaAltura))
    teste = abreFase(personagem.fase)
    AtualizaMuros(teste)
    teste = maca.Muda(fase=teste, tileY=tileY, tileX=tileX)
    teste = macaPodre.Muda(fase=teste, tileY=tileY, tileX=tileX)
    while True:
        imgFase = font.render(nomeFase[n-1], True, preto)
        imgContinue = font.render("Aperte ENTER para CONTINUAR", True, preto)
        imgMenu = font.render("Aperte ESC para voltar ao MENU", True, preto)
        tela.fill((0, 0 ,0))
        tela.blit(imgFase, (400, 350))
        tela.blit(imgContinue, (0, 650))
        tela.blit(imgMenu, (0, 670))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 6
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 1
                if event.key == pygame.K_RETURN:
                    return 0
def Jogar():
    global s, tela, personagem, maca, macaPodre, teste, Nfase
    font = pygame.font.Font('fontes/TlwgTypist-Bold.ttf', 25)
    AtualizaMuros(teste)
    s = 600
    tick = 0
    segundos = 120
    imgSegundos = font.render('Tempo:'+str(segundos),True, preto)
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
            segundos -= 1
            imgSegundos = font.render('Tempo:' + str(segundos), True, preto)
            tick = 0

        if personagem.TestaMaca(maca.rect):
            teste = maca.Muda(fase=teste, tileY=tileY, tileX=tileX)

        if personagem.TestaMacaPodre(macaPodre.rect):
            teste = macaPodre.Muda(fase=teste, tileY=tileY, tileX=tileX)

        if maca.segundo >= 5:
           teste = maca.Muda(fase=teste, tileY=tileY, tileX=tileX)

        if macaPodre.segundo >= 5:
           teste = macaPodre.Muda(fase=teste, tileY=tileY, tileX=tileX)

        if personagem.ponto < 0 or segundos == 0:
            return 7
        if personagem.fase == 0:
            if MudaFase(1):
                return 1
        if personagem.ponto >= 100 and personagem.fase == 1:
            if MudaFase(2):
                return 1
        if personagem.ponto >= 200 and personagem.fase == 2:
            if MudaFase(3):
                return 1
        if personagem.ponto >= 400 and personagem.fase == 3:
            MudaFase(4)
        if personagem.ponto >= 800 and personagem.fase == 4:
            MudaFase(5)
        if personagem.ponto >= 1600 and personagem.fase == 5:
            return 1

        tela.blit(fundo, (0, 0))
        tela.blit(imgSegundos, (200, 0))
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                for muro in muros:
                    if muro.collidepoint(pygame.mouse.get_pos()):
                        print("clicado no muro")

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
