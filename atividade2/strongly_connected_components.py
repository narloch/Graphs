from parser_arquivo import parser_arquivo
from grafo import Grafo

import math
import sys



# Algoritmo 17
def dfs_visit(G, v, C, T, A, F, time):
    C[G.vertices.index(v)] = True
    time[0] = time[0] + 1
    T[G.vertices.index(v)] = time[0]

    # saintes de v
    # castamos para int pois math.inf eh um float. The more you know.
    out_v = [G.vertices[int(vertex)]
            for vertex in range(len(G.mapa_arestas[G.vertices.index(v)]))
            if G.mapa_arestas[G.vertices.index(v)][vertex] != math.inf]
            
    for u in out_v:
        if not C[G.vertices.index(u)]:
            A[G.vertices.index(u)] = v
            dfs_visit(G, u, C, T, A, F, time)
    
    time[0] = time[0] + 1
    F[G.vertices.index(v)] = time[0]



# Algoritmo 16a
def dfs_cormen(G):
    C = [False for i in range(G.qnt_Vertices())]
    T = [math.inf for i in range(G.qnt_Vertices())]
    F = [math.inf for i in range(G.qnt_Vertices())]
    A = [None for i in range(G.qnt_Vertices())]

    time = [0]

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

    time = [0]

    for u in sorted_F.values():
        if not C[u]:
            dfs_visit(G, G.vertices[u], C, T, A, F, time)
    
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
    
    g_dash = Grafo(transposed_vertex, transposed_edges, transposed_map)

    return g_dash



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
components = []

copy_A_t = A_t.copy()

# marca o ultimo indice em que None foi encontrado
last_ocurrence_of_none = 0

# filtra os vertices que nao tem ancestrais
for _ in copy_A_t:
    if _ is None:
        components.append([graph.vertices[A_t.index(_, last_ocurrence_of_none)]])
        last_ocurrence_of_none = copy_A_t.index(_) + 1
        copy_A_t.remove(_)

while len(copy_A_t):
    ancestor_v = copy_A_t.pop(0)
    found_ancestor = False

    for component in components:
        if ancestor_v in component:
            component.append(graph.vertices[A_t.index(ancestor_v)])
            found_ancestor = True
            break
    
    # retorna pra lista para ser procurado novamente mais tarde
    if not found_ancestor:
        copy_A_t.append(ancestor_v)

for component in components:
    print(', '.join(component))