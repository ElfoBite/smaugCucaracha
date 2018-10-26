file = open ("./file1.txt", "r").read()
file2 = open("./file2.txt", "w")

i=0

strin=""

lst = []
for line in file:
    for ch in line:
        lst.append(ch)
cod = len(lst)

d=0

while d < cod:
    if lst[d] == " ":
        i += 1

    elif i>0:
        strin +="*"
        strin +=str(i)
        i=0

    if lst[d] != " ":
        strin+=lst[d]
    d+=1


file2.write(strin)
file2.close()

