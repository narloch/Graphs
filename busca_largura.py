from parser_arquivo import parser_arquivo
from grafo import Grafo
import sys
import math
from collections import OrderedDict

nome_arquivo = sys.argv[1]
s = int(sys.argv[2])
with open(nome_arquivo) as f:
    arquivo_grafo = f.read().splitlines()

vertices, arestas, mapa_arestas = parser_arquivo(arquivo_grafo)
grafo = Grafo(vertices, arestas, mapa_arestas)

conhecidos = [False for i in grafo.vertices]
distancia = [math.inf for i in grafo.vertices]
fila = set()

conhecidos[s-1] = True
distancia[s-1] = 0
fila.add(s)

while fila:
    u = fila.pop()
    for i in grafo.vizinhos(u):
        if conhecidos[i-1] == False:
            conhecidos[i-1] = True
            distancia[i-1] = distancia[u-1]+1
            fila.add(i)

nivel = set(distancia)
if math.inf in nivel: nivel.remove(math.inf)
for i in nivel:
    N = [j+1 for j in range(len(distancia)) if distancia[j] == i]
    print(str(i)+': '+','.join(map(str, N)))
