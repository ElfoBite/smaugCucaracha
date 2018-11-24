import pygame
import os

# variaveis onde guardamos as nossas texturas
_images = {}
_sounds = {}
_music = {}

# caminho para a nossa pasta res
_root_directory = os.path.dirname(os.path.realpath(__file__)) + "/res/"

# Limpa tudo o que estiver em cache
def clear():
    clear_images()
    clear_music()
    clear_sounds()

# Limpa a cache de imagens
def clear_images():
    del _images

# limpa a cache de sons
def clear_sounds():
    del _sounds

# limpa a cache de musicas
def clear_music():
    del _music

# obtem uma imagem da pasta characters
# filename -> nome da imagem.extensao
def characters(filename):
    filename = "graphics/characters/{0}".format(filename)
    if not filename in _images.keys():
        _images[filename] = _load_surface_from_disk(_root_directory + filename)
    return _images[filename]

# obtem uma imagem da pasta backgronds
# filename -> nome da imagem.extensao
def backgrounds(filename):
    filename = "graphics/backgrounds/{0}".format(filename)
    if not filename in _images.keys():
        _images[filename] = _load_surface_from_disk(_root_directory + filename)
    return _images[filename]

# obtem uma imagem da pasta tilesets
# filename -> nome da imagem.extensao
def tilesets(filename):
    filename = "graphics/tilesets/{0}".format(filename)
    if not filename in _images.keys():
        _images[filename] = _load_surface_from_disk(_root_directory + filename)
    return _images[filename]

# obtem uma imagem da pasta animations
# filename -> nome da imagem.extensao
def animations(filename):
    filename = "graphics/animations/{0}".format(filename)
    if not filename in _images.keys():
        _images[filename] = _load_surface_from_disk(_root_directory + filename)
    return _images[filename]

# obtem uma imagem da pasta images
# filename -> nome da imagem.extensao
def images(filename):
    filename = "graphics/images/{0}".format(filename)
    if not filename in _images.keys():
        _images[filename] = _load_surface_from_disk(_root_directory + filename)
    return _images[filename]

# carrega uma imagem de um local do disco
# filename -> caminho completo para a imagem
def load_graphics_from_file(filename):
    if not filename in _images.keys():
        _images[filename] = _load_surface_from_disk(filename)
    return _images[filename]

# metodo interno para carregar imagens
def _load_surface_from_disk(filename):
    return pygame.image.load(filename)