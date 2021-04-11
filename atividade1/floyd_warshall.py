from parser_arquivo import parser_arquivo
from grafo import Grafo
import sys
import math

nome_arquivo = sys.argv[1]
with open(nome_arquivo) as f:
    arquivo_grafo = f.read().splitlines()

vertices, arestas, mapa_arestas = parser_arquivo(arquivo_grafo)
grafo = Grafo(vertices, arestas, mapa_arestas)

distancia = grafo.mapa_arestas

num_vertices = range(grafo.qnt_Vertices())
for k in num_vertices:
    for i in num_vertices:
        for j in num_vertices:
            distancia[i][j] = min(distancia[i][j], 
                                distancia[i][k] + distancia[k][j])

for v in num_vertices:
    print(str(v+1)+": "+','.join(map(str, distancia[v])))