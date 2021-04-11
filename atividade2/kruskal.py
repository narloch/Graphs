from parser_arquivo import parser_arquivo
from grafo import Grafo

import math
import sys

with open("grafo.txt") as f:
    arquivo_grafo = f.read().splitlines()

vertices, arestas, mapa_arestas = parser_arquivo(arquivo_grafo)
grafo = Grafo(vertices, arestas, mapa_arestas)

arvore = []
s = [[v] for v in range(grafo.qnt_Vertices())]

# pode rir professor, o desespero é o pai da gambiarra
dic_arestas = {grafo.peso(aresta[0], aresta[1]): aresta for aresta in grafo.arestas}
arestas_ordenadas = [dic_arestas[chave] for chave in sorted(dic_arestas.keys())]

for aresta in arestas_ordenadas:
    if s[aresta[0]-1] != s[aresta[1]-1]:
        arvore = arvore + [aresta]
        x = s[aresta[0]-1] + s[aresta[1]-1]
        for y in x:
            s[y-1] = x

print(sum([grafo.peso(aresta[0], aresta[1]) for aresta in arvore]))
print(*(str(aresta[0]) + '-' + str(aresta[1]) for aresta in arvore), sep= ', ')
