import heapq
from collections import defaultdict


def encode(frequencia):
    heap = [[peso, [simbolo, '']] for simbolo, peso in frequencia.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for par in lo[1:]:
            par[1] = '0' + par[1]
        for par in hi[1:]:
            par[1] = '1' + par[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


data = "huffman atividade para a professora magali, nao é o melhor, mas ao menos eu tentei"
frequencia = defaultdict(int)
for simbolo in data:
    frequencia[simbolo] += 1

huff = encode(frequencia)
print ("simbolo".ljust(10) + "peso".ljust(10) + "Huffman codigo bytes")
for p in huff:
    print (p[0].ljust(10) + str(frequencia[p[0]]).ljust(10) + p[1])