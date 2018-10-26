file2 = open("./file2.txt", "r").read()
file3 = open("./file3.txt", "w")

lst2 = []
numero = 0

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

descompress = False
for ch in file2:
    if ch == "*":
        descompress = True
    elif descompress:
        if is_number(ch):
            numero *= 10
            numero += int(ch)
        else:
            lst2.append(' ' * numero)
            lst2.append(ch)
            numero = 0
            descompress = False
    else:
        lst2.append(ch)

res = str(lst2)

we = 0
wo = len(lst2)
res = ""
while we < wo:
    res += lst2[we]
    we += 1

file3.write(res)

