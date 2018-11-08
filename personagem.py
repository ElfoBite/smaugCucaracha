import pygame

class Personagem(object):

    x = 0
    y = 0
    largura = 60
    altura = 25
    moveX = 0
    moveY = 0
    velocidade = 5

    ativo = pygame.image.load('img/Cockroach Type 1 Color 1 Move 1.png')
    direita = pygame.transform.scale(ativo, (largura, altura))
    esquerda = pygame.transform.flip(direita, True, False)

    ativo = pygame.image.load('img/Cockroach2Move1.png')
    cima = pygame.transform.scale(ativo, (altura, largura))
    baixo = pygame.transform.flip(cima, False, True)

    ativo = direita

    def __init__(self, altura, largura):
        self.x = altura/2
        self.y = largura/2

    def AndaDireita(self):
        self.moveX = self.velocidade
        self.moveY = 0
        self.ativo = self.direita

    def AndaEsquerda(self):
        self.moveX = -(self.velocidade)
        self.moveY = 0
        self.ativo = self.esquerda

    def AndaCima(self):
        self.moveY = -(self.velocidade)
        self.moveX = 0
        self.ativo = self.cima

    def AndaBaixo(self):
        self.moveY = self.velocidade
        self.moveX = 0
        self.ativo = self.baixo

    def ParaX(self):
        self.moveX = 0

    def ParaY(self):
        self.moveY = 0

    def TestaLimiteDaTela(self,largura,altura):
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > largura - self.largura:
            self.x = largura - self.largura
        if self.y > altura - self.largura:
            self.y = altura - self.largura


    def rect(self):
        return pygame.Rect((self.x, self.y), self.ativo.get_size())

    def TestaMuro(self, muros):
        for muro in muros:
            if self.rect().colliderect(muro):
                self.x -= self.moveX * 2
                self.y -= self.moveY * 2

    def TestaMaca(self,maca):
            if self.rect().colliderect(maca):
                return 1
            return 0