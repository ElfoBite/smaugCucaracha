
import pygame
#import mapa tiles

class Character(pygame.Rect):

	largura, altura = 40,40

	# ... construtor de objetos ...
	def __init__(self,x,y):
		pygame.Rect.__init__(self, x, y, Character.largura, Character.altura)

	def __str__(self):
		return str(self.get_number())


	def get_number(self):
		return ((self.x / self.largura)+ Tile.H) + ((self.y / self.altura)* Tile.V)

	def get_tile(self):
		return Tile.get_tile(self.get_number)

#=============="controles" para quadros da animacao dos sprites======================
a = 0
b = 0
largura = 40
altura = 40
frame = 0.0




## teste  personagem inimigo



class Inimigo(Character):
    Character.__init__(self, x, y)
    Inimigo.Lista.append(self)

def draw(self, tela):
    global a, b, largura, altura, frame

    caminho = os.path.join("")

    if frame >= 1.0:
        a += 40
        frame = 0.0

    frame += 0.1

    if a >= (40 * 6):
        a = 0

    for Inimigo in Inimigo.Lista:
        Inimigo = pygame.image.load(caminho).convert_alpha()
        tela.blit(Inimigo, (self.x, self.y), (a, b, largura, altura))




