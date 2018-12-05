import zlib
def compress(arquivo):
    my_data = open(arquivo, 'rb').read()
    arquivo = arquivo.split('.')
    arquivo = arquivo[0]
    compressed_data = zlib.compress(my_data, 9)

    f = open(arquivo+'.dat', 'wb')
    f.write(compressed_data)
    f.close()

def descompress(arquivo):
    my_data = open(arquivo, 'rb').read()
    arquivo = arquivo.split('.')
    arquivo = arquivo[0] + '.descompress'
    descompress_data = zlib.decompress(my_data)

    f = open(arquivo, 'wb')
    f.write(descompress_data)
    f.close()


compress('Cenarios/fase0 - Copia.txt')
descompress("Cenarios/fase0 - Copia.dat")