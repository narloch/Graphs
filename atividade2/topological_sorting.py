from parser_arquivo import parser_arquivo
from grafo import Grafo
import sys
import math


def dfs_ordenacao_topologica(grafo):
    conhecido = [False for v in grafo.vertices]
    tempo_acesso = [math.inf for v in grafo.vertices]
    final = [math.inf for v in grafo.vertices]
    tempo = 0

    ordenacao = []

    for u in range(grafo.qnt_Vertices()-1):
        if conhecido[u-1] == False:
            conhecido, tempo_acesso, final, tempo, ordenacao = dfs_vist_ot(grafo, u, conhecido, tempo_acesso, final, tempo, ordenacao)

    return ordenacao


def dfs_vist_ot(grafo, v, conhecido, tempo_acesso, final, tempo, ordenacao):
    
    conhecido[v-1] = True
    tempo = tempo + 1
    tempo_acesso[v-1] = tempo

    for u in grafo.vizinhos(v-1):
        if conhecido[u-1] == False:
            conhecido, tempo_acesso, final, tempo, ordenacao = dfs_vist_ot(grafo, u, conhecido, tempo_acesso, final, tempo, ordenacao)

    tempo = tempo + 1
    final[v-1] = tempo
    ordenacao.insert(0, v-1)

    return conhecido, tempo_acesso, final, tempo, ordenacao

with open("grafo.txt") as f:
    arquivo_grafo = f.read().splitlines()

vertices, arestas, mapa_arestas = parser_arquivo(arquivo_grafo)
grafo = Grafo(vertices, arestas, mapa_arestas)

ordem = dfs_ordenacao_topologica(grafo)

print(*[grafo.rotulo(o+1) for o in ordem], sep=' → ')
