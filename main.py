from parser_arquivo import parser_arquivo
from grafo import Grafo

with open("grafo.txt") as f:
    arquivo_grafo = f.read().splitlines()

vertices, arestas, mapa_arestas = parser_arquivo(arquivo_grafo)
grafo = Grafo(vertices, arestas, mapa_arestas)

