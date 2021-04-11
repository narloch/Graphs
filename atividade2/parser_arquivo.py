import math

def parser_arquivo(arquivo):
    n = int(arquivo[0].split()[-1])
    vertices = [arquivo[i].split()[-1] for i in range(1, n+1)]
    arestas = list()
    mapa_arestas = [[math.inf if i!=j else 0 for i in range(n)] for j in range(n)]

    isPonderado = True if arquivo[n+1] == '*arc' else False

    for i in range(n+2, len(arquivo)):
        x, y, peso = [int(i) for i in arquivo[i].split()]
        arestas.append([x, y])
        mapa_arestas[x-1][y-1] = int(peso)

        if not isPonderado:
            mapa_arestas[y-1][x-1] = int(peso)

    return vertices, arestas, mapa_arestas
    