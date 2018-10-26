file = open('./file2.txt', 'r').read()
file2 = open('./file3.txt', 'w')

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

lst2 = []
numero = 0
descompress = False
ant = ''
i = ''
for ch in file:
    if ch == "*":
        descompress = True
        i = ant
    elif descompress:
        if is_number(ch):
            numero *= 10
            numero += int(ch)
        else:
            lst2.append(i * int(numero))
            lst2.append(ch)
            numero = 0
            descompress = False
    else:
        lst2.append(ch)

    ant = ch
arq = ''
for ch in lst2:
    arq = arq + str(ch)

file2.write(arq)
file2.close()