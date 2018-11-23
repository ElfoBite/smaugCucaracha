def abreFase(fase):
    arquivo = open(fase)
    teste = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    y = 0
    for i in arquivo:
        for j in i:
            if not(j == '\n'):
                teste[y].append(int(j))
        y += 1
    return teste
