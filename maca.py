import pygame
import random

class Maca(object):
    tick = 600
    x = 0
    y = 0

    img = pygame.image.load('img/maca.png')
    rect = pygame.Rect(0, 0, 0, 0)
    tileX = 0
    tileY = 0
    segundo = 0
    tipo = 2

    def __init__(self, tileX, tileY, podre):
        self.tileX = tileX
        self.tileY = tileY
        if podre:
            self.img = pygame.image.load('img/macaPodre.png')
            self.tipo = 3
        self.img = pygame.transform.scale(self.img, (self.tileX, self.tileY))

    def Muda(self, fase, tileY, tileX):
        y = 0
        for i in fase:
            x = 0
            for j in i:
                if j == self.tipo:
                    fase[y][x] = 0
                x += 1
            y += 1

        while True:

            y = random.randint(0, 22)
            x = random.randint(0, 31)

            if fase[y][x] == 0:
                fase[y][x] = self.tipo

                self.x = x * tileX
                self.y = y * tileY

                self.rect = pygame.Rect(self.x, self.y, tileX, tileY)
                self.tick = 0
                return fase
