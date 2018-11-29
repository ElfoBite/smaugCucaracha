def criaDicionario(n):
    file = open('Cenarios/fase'+str(n)+'.mtx', 'r').read()
    file2 = open('Cenarios/fase'+str(n)+'.dic', 'w')
    ant = 0
    linhas = []
    lista = []
    linha = ''
    for ch in file:
        if not(ch == ant) and not(lista == []):
            for l in lista:
                linha += l
            linhas.append(linha)
            lista = []
            linha = ''
        else:
            lista.append(ch)
            ant = ch
    arq = ''
    for l in (sorted(set(linhas), reverse=True)):
        if not(l == '\n'):
            arq = arq + l + '\n'
    file2.write(arq)

def leDicionario(n):
    file = open('Cenarios/fase' + str(n) + '.dic', 'r').read()
    ch = 'A'
    dicionario = {}
    linha = ''
    for l in file:
        if l == '\n':
            dicionario[ch] = linha
            ch = chr((ord(ch)+1))
            linha = ''
        else:
            linha = linha + l
    return dicionario

def comprime(n):
    file = open('Cenarios/fase' + str(n) + '.mtx', 'r').read()
    file2 = open('Cenarios/fase'+str(n)+'.cps', 'w')
    criaDicionario(n)
    dicionario = leDicionario(n)
    for D in dicionario:
        file = file.replace(dicionario[D], D)
    file2.write(file)

def descomprime(n):
    file = open('Cenarios/fase'+str(n)+'.cps', 'r').read()
    dicionario = leDicionario(n)
    ch = ''
    arq = []
    for l in file:
        arq.append(l)
    for l in arq:
        if l == '\n' or l == '0':
            ch += l
        else:
            ch += dicionario[l]
    return ch

    comprime(i)
