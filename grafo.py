import math


class Grafo:
    def __init__(self, vertices, arestas, mapa_arestas):
        self.vertices = vertices
        self.arestas = arestas
        self.mapa_arestas = mapa_arestas

    def qnt_Vertices(self):
        return len(self.vertices)

    def qnt_Arestas(self):
        return len(self.arestas)

    def grau(self, v):
        arestas_v = self.mapa_arestas[v-1]
        return (len(arestas_v) - arestas_v.count(math.inf))

    def rotulo(self, v):
        return self.vertices[v-1]

    def vizinhos(self, v):
        return [i+1 for i in range(len(self.mapa_arestas)) if self.mapa_arestas[v-1][i] != math.inf]

    def haAresta(self, u, v):
        return True if self.mapa_arestas[u-1][v-1] != math.inf else False

    def peso(self, u, v):
        return self.mapa_arestas[u-1][v-1]
