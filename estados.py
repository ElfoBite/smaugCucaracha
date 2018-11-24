import pygame
from menu import TelaInicial, Menu, Loja
from jogo import Jogar, GameOver

try:
    pygame.init()
except:
    print("O modulo pygame não foi iniciado com sucesso")

estado = 0

while True:
    print(estado)
    if estado == 0:
        estado = TelaInicial()
    elif estado == 1:
        estado = Menu()
    elif estado == 2:
        estado = Jogar()
    elif estado == 3:
        pass
        #configuração
    elif estado == 4:
        estado = Loja()
    elif estado == 5:
        pass
        #Pause
    elif estado == 6:
        pygame.quit()
        exit()
    elif estado == 7:
        estado = GameOver()

