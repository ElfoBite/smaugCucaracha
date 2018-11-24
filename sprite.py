import cache
import graphics
import pygame


class Sprite:
    # construtor da nossa classe
    # podemos passar uma string  ou uma imagem diretamente
    def __init__(self, filename=None, image=None):
        self.src_rect = None
        self.position = pygame.Rect(0, 0, 1, 1)
        self.z = 0
        self._loaded = False
        self.visible = True
        self._data = image
        self.filename = filename

    # metodo responsavel por desenhar o nosso sprite
    def draw(self, surface):
        # se tivermos uma imagem carregada
        if self._data:
            # defenimos o nosso rectangulo de destino para ter a mesma largura e altura que o nosso src_rect
            self.position.width = self.src_rect.width
            self.position.height = self.src_rect.height
            # desenhamos o sprite no nosso surface
            surface.blit(self._data, self.position, self.src_rect)

    # metodo responsavel por carregar uma imagem para o nosso sprite
    # deve ser chamado no game.load_content()
    def load_image(self, filename):
        # se ja existir a imagem devemos eliminar
        # para libertamos recursos
        if self._data:
            del self._data
        # caqrregamos a imagem do nosso cache
        self._data = cache.images(filename)
        # convertemos para ter uma camada suave no alpha
        self._data.convert_alpha()
        self.src_rect = self._data.get_rect()

        self.position.width = self.src_rect.width
        self.position.height = self.src_rect.height

    # Limpamos a nossa imagem para liberar recursos
    def dispose(self):
        del self._data
        self.filename = None
        self._loaded = False

    # este metodo serve para informar o modulo
    # graphics que deve desenhar este sprite
    # todos os frames
    def auto_draw(self, autodraw):
        if autodraw:
            graphics.add_sprite(self)
        else:
            graphics.remove_sprite(self)

    # Getters e setters
    def get_x(self):
        return self.position.x

    def get_y(self):
        return self.position.y

    def set_x(self, value):
        self.position.x = value

    def set_y(self, value):
        self.position.y = value

    # propriedades
    x = property(get_x, set_x)
    y = property(get_y, set_y)