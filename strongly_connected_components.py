from parser_arquivo import parser_arquivo
from grafo import Grafo

import math
import sys



# Algoritmo 17
def dfs_visit(G, v, C, T, A, F, time):
    # aliasing
    index_v = G.vertices.index(v)

    C[index_v] = True
    time = time + 1
    T[index_v] = time

    print(G.mapa_arestas)

    # saintes de v
    out_v = [vertex for vertex in G.mapa_arestas[index_v] 
            if G.mapa_arestas[index_v][vertex] != math.inf]

    print(out_v)

    for u in out_v:
        if not C[u]:
            A[u] = v
            dfs_visit(G, u, C, T, A, F, time)
    
    time = time + 1
    F[G.index(v)] = time



# Algoritmo 16a
def dfs_cormen(G):
    C = [False for i in range(G.qnt_Vertices())]
    T = [math.inf for i in range(G.qnt_Vertices())]
    F = [math.inf for i in range(G.qnt_Vertices())]
    A = [None for i in range(G.qnt_Vertices())]

    time = 0

    for u in G.vertices:
        if not C[G.vertices.index(u)]:
            dfs_visit(G, u, C, T, A, F, time)
    
    return (C, T, A, F)



# Algoritmo 16b - mesmo que acima, mas percorre os vertices de acordo com a
# ordenacao decrescente de F
def dfs_cormen_b(G, sorted_F):
    C = [False for i in range(G.qnt_Vertices())]
    T = [math.inf for i in range(G.qnt_Vertices())]
    F = [math.inf for i in range(G.qnt_Vertices())]
    A = [None for i in range(G.qnt_Vertices())]

    time = 0

    for u in sorted_F.values():
        if not C[G.index(u)]:
            dfs_visit(G, u, C, T, A, F, time)
    
    return (C, T, A, F)



# funcao auxiliar para transpor o grafo, implementa as linhas 2 a 5 do
# algoritmo 15 (e retorna o G^T)
# entrada: grafo G; saida: grafo G^T
def transpose(G):
    transposed_vertex = G.vertices
    transposed_edges = G.arestas
    transposed_map = [[] for _ in range(G.qnt_Vertices())]

    for i in range(G.qnt_Vertices()):
        for j in range(G.qnt_Vertices()):
            transposed_map[i].append(G.mapa_arestas[j][i])

    return Grafo(transposed_vertex, transposed_edges, transposed_map)



# Algoritmo 15
def strongly_connected_components(G):
    C, T, A_dash, F = dfs_cormen(G)

    G_t = transpose(G)

    # funciona porque o vetor F nao tem numeros repetidos
    sorted_F = {f : F.index(f) for f in sorted(F, reverse=True)}

    # como nao utilizaremos os outros vetores retornados a convencao eh
    # associa-los a _
    (_, _, A_dashT, _) = dfs_cormen_b(G_t, sorted_F)

    return A_dashT



file_name = sys.argv[1]
with open(file_name) as f:
    graph_archive = f.read().splitlines()

vertex, edges, edges_map = parser_arquivo(graph_archive)
graph = Grafo(vertex, edges, edges_map)

# cada arvore retornada eh uma componente fortemente conexa
A_t = strongly_connected_components(graph)


