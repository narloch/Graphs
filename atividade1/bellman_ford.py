from parser_arquivo import parser_arquivo
from grafo import Grafo
import sys
import math

nome_arquivo = sys.argv[1]
s = int(sys.argv[2])
with open(nome_arquivo) as f:
    arquivo_grafo = f.read().splitlines()

vertices, arestas, mapa_arestas = parser_arquivo(arquivo_grafo)
grafo = Grafo(vertices, arestas, mapa_arestas)

distancia = [math.inf for _ in grafo.vertices]
distancia[s-1] = 0

arestas = grafo.arestas + [[j]+[i] for [i, j] in grafo.arestas]
caminho = [[] for i in grafo.vertices]

for i in range(grafo.qnt_Vertices()-1):
    for aresta in arestas:
        u = aresta[0]
        v = aresta[1]
        if distancia[u-1] != math.inf and distancia[v-1] > (distancia[u-1] + grafo.peso(u, v)):
            distancia[v-1] = distancia[u-1] + grafo.peso(u, v)
            caminho[v-1] = caminho[u-1] + [u]

for aresta in arestas:
    u = aresta[0]
    v = aresta[1]
    if distancia[v-1] > (distancia[u-1] + grafo.peso(u, v)):
        print("Ciclo de peso negativo encontrado")
        sys.exit()

for i in range(len(distancia)):
    caminho[i].append(i+1)
    print(str(i+1)+": " +
          ','.join(map(str, caminho[i]))+"; d="+str(distancia[i]))
