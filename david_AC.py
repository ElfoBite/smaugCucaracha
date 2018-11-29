#teste
import pygame
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
x1 = 20
y1 = 10
x2 = 700
y2 = 10
movex1 = 0
movey1 = 0
movex2 = 0
movey2 = 0
vermelho = (255, 0, 0)
amarelo = (255, 255, 0)
while True:
    x1 += movex1
    y1 += movey1
    x2 += movex2
    y2 += movey2
    if x1 <= 0:
        x1 -= movex1
    if x1 <= 800:
        x1 -= movex1
    if y1 <= 0:
        y1 -= movey1
    if


    if x2 <= 0:
        x2 -= movex2

    tela.fill ((0, 0, 0))

    r1 = pygame.Rect(x1, y1, 50, 30)
    pygame.draw.rect(tela, vermelho, r1)
    r2 = pygame.Rect(x2, y2, 50, 30)
    pygame.draw.rect(tela, amarelo, r2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                movey1 = 1
            if event.key == pygame.K_w:
                movey1 = -1
            if event.key == pygame.K_a:
                movex1 = -1
            if event.key == pygame.K_d:
                movex1 = 1
            if event.key == pygame.K_DOWN:
                movey2 = 1
            if event.key == pygame.K_UP:
                movey2 = -1
            if event.key == pygame.K_LEFT:
                movex2 = -1
            if event.key == pygame.K_RIGHT:
                movex2 = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                movey1 = 0
            if event.key == pygame.K_w:
                movey1 = 0
            if event.key == pygame.K_a:
                movex1 = 0
            if event.key == pygame.K_d:
                movex1 = 0
            if event.key == pygame.K_DOWN:
                movey2 = 0
            if event.key == pygame.K_UP:
                movey2 = 0
            if event.key == pygame.K_LEFT:
                movex2 = 0
            if event.key == pygame.K_RIGHT:
                movex2 = 0
    pygame.display.update()