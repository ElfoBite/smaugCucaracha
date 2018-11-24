import pygame
from fase import abreFase

pygame.init()
telaLargura = 960
telaAltura = 690
fase = 2
img = 'Cenarios/fase'+str(fase)+'.png'

tela = pygame.display.set_mode((telaLargura, telaAltura), pygame.DOUBLEBUF, 32)

fase = abreFase('Cenarios/fase'+str(fase))

tileX = int(telaLargura / 32)
tileY = int(telaAltura / 23)


fundo = pygame.image.load(img)
fundo = pygame.transform.scale(fundo, (telaLargura, telaAltura))

while True:
    tela.blit(fundo, (0, 0))

    y = 0
    for i in fase:
        x = 0
        for j in i:
            if j == 1:
                pygame.draw.rect(tela, (0, 0, 0), (x, y, tileX, tileY))
            x += tileX
        y += tileY

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
