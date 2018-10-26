file = open('./file1.txt', 'r').read()
file2 = open("./file2.txt", 'w')

ant = ''
i = 0
arq = []


for ch in file:
    if ch == ant:
        i += 1
    elif i > 0:
        arq.append('*')
        arq.append(str(i))
        arq.append(ch)
        i = 0
    else:
        arq.append(ch)
    ant = ch

letra = ''

for ch in arq:
    letra = letra + str(ch)

file2.write(letra)
file2.close()