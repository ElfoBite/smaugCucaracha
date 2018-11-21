#"Modulo graphics, modulo responsavel por tratar dos graphicos do jogo"
import pygame

_instance = None


def get_context():
    global _instance
    return _instance


def add_sprite(sprite):
    if sprite not in get_context().sprites:
        get_context().sprites.append(sprite)


def remove_sprite(sprite):
    if sprite in get_context().sprites:
        get_context().sprites.remove(sprite)


class Graphics:
    def __init__(self, width, height, title):
        self.surface = pygame.display.set_mode((width, height), pygame.HWSURFACE)
        pygame.display.set_caption(title)
        pygame.display.flip()
        # Adicionamos um arrays de sprites que precisam de ser desenhados
        self.sprites = []
        # flag que controla se devemos limpar o ecra a cada frame
        self.auto_clear = True
        # defenimos a variavel _instance para ser este objeto
        # isto e uma singleton class
        global _instance
        _instance = self

    def update(self):
        pygame.display.update()

    def fullscreen(self, fullscreen):
        pass

    def bitmap(self):
        return self.surface

    def draw(self):
        if self.auto_clear:
            self.clear()

        for sp in sorted(self.sprites, key=lambda sprite: sprite.z):
            sp.draw(surface=self.surface)

    def clear(self, color=(30, 30, 30)):
        self.surface.fill(color)