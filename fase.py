from compressfases import descomprime
def abreFase(fase):
    arquivo = descomprime(fase)
    teste = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    y = 0
    for i in arquivo:
        if not(i == '\n'):
            teste[y].append(int(i))
        else:
            y += 1
    return teste