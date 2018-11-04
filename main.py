from menu import TelaInicial, Menu
from jogo import Jogar

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
        pass
        #Loja
    elif estado == 5:
        pass
        #Pause
    elif estado == 6:
        exit()
