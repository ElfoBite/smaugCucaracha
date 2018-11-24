#classe game, responsavel por tratar de todo o jogo
import  pygame
import graphics
import os
import input
from sprite import*

class Game:
# Construtor da class Game
# aqui defenimos todas as variaveis de instancia
    logo = None
    def __init__(self, width=800, height=600, title="Carrera de la Cucaracha", fullscreen=True):
        self.Graphics = graphics.Graphics(width, height, title)
        self.spr = Sprite()
        # verificamos se apresentamos em fullscreen ou janela
        if fullscreen:
            pygame.display.toggle_fullscreen()
        # criamos um objeto clock para tratarmos os fps do nosso jogo
        self.clock = pygame.time.Clock()
        # iniciamos esta flag para verdadeiro, assim para fecharmos o processo do jogo
        # basta defenir esta variavel como False
        self.running = True
    def update(self, gametime=None):
        if gametime is None:
            gametime = self.get_last_gametime()
        input.update()
        self.spr.position.center = input.mouse_pos()
    def draw(self, surface=None):
        self.Graphics.draw()
        #aqui é o espaço para desenhar mais coisas
        self.Graphics.update()
        self.tick(30)
        self.Graphics.update()
    def tick(self, fps):
        pass
    def get_last_gametime(self):
        return 0
    def load_content(self):
         Game.logo = pygame.image.load('res/graphics/images/logo.png')
         self.spr.auto_draw(True)
    def unload_content(self):
        pass