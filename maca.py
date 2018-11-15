import pygame
import random

class Maca(object):
    tick = 600
    x = 0
    y = 0
    img = pygame.image.load('img/maca.jpg')
    rect = pygame.Rect(0, 0, 0, 0)
    tileX = 0
    tileY = 0
    segundo = 0

    def __init__(self, tileX, tileY):
        self.tileX = tileX
        self.tileY = tileY
        self.img = pygame.transform.scale(self.img, (self.tileX, self.tileY))

    def Muda(self, fase, tileY, tileX):
        y = 0
        for i in fase:
            x = 0
            for j in i:
                if j == 2:
                    fase[y][x] = 0
                x += 1
            y += 1

        while True:

            self.y = random.randint(0,22)
            self.x = random.randint(0,31)

            if fase[self.y][self.x] == 0:
                fase[self.y][self.x] = 2

                self.x = self.x * tileX
                self.y = self.y * tileY

                self.rect = pygame.Rect(self.x, self.y, tileX, tileY)
                self.tick = 0
                return fase