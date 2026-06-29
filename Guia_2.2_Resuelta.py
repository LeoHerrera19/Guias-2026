
#Implementar la función `bfs_orden(G, inicio)` que retorne una lista con los nodos en el orden en que son visitados por el algoritmo BFS.

from collections import deque
import networkx as nx


def bfs_orden(G, inicio):
    lista = []
    q = deque()

    visitado = {x: False for x in G.nodes}
    visitado[inicio] = True
    q.append(inicio)

    while q:
        v = q.popleft()
        lista.append(v)

        for w in G.neighbors(v):
            if visitado[w] == False:
                visitado[w] = True
                q.append(w)
    return lista

#Implementar `bfs_distancias(G, inicio)` que retorne un diccionario con la distancia mínima (número de aristas) desde el nodo de inicio a todos los demás nodos alcanzables.

def bfs_distancias(G, inicio):
    distancias = {x: None for x in G.nodes}

    q = deque()

    visitado = {x: False for x in G.nodes}
    visitado[inicio] = True
    q.append(inicio)

    while q:
        v = q.popleft()

        for w in G.neighbors(v):
            if visitado[w] == False:
                visitado[w] = True
                q.append(w)
                distancias[w] =  distancias[v] + 1
    return distancias

#Implementar `bfs_camino(G, inicio, fin)` que retorne una lista con los nodos que forman el camino más corto entre `inicio` y `fin`. Si no hay camino, retornar `None`.

def bfs_camino(G, inicio, fin):
    q = deque()

    padres = {x: None for x in G.nodes}
    
    visitado = {x: False for x in G.nodes}
    visitado[inicio] = True
    q.append(inicio)
    camino_encontrado = False

    while q:
        v = q.popleft()
        if v == fin:
            camino_encontrado = True
            break
      
        for w in G.neighbors(v):
            if visitado[w] == False:
                visitado[w] = True
                padres[w] = v
                q.append(w)
        
    if camino_encontrado == False:
        return None
    
    camino = []
    actual = fin

    while actual is not None:
        camino.append(actual)
        actual = padres[actual]
    
    return camino[::-1]

#Implementar el recorrido DFS de forma recursiva. La función `dfs_recursivo(G, nodo, visitados=None)` debe retornar el conjunto de nodos visitados.

def dfs_recursivo(G, nodo, visitados=None):
    if visitados is None:
        visitados = set()

    visitados.add(nodo)

    for w in G.neighbors(nodo):
        if w not in visitados:
            dfs_recursivo(G, w, visitados)


    return visitados

#Implementar el recorrido DFS utilizando una pila (LIFO) de forma iterativa.

def dfs_iterativo(G, inicio):
    p = []
    visitados = set()

    visitados.add(inicio)
    p.append(inicio)

    while p:
        v = p.pop()
        for w in G.neighbors(v):
            if w not in visitados:
                visitados.add(w)
                p.append(w)

    return visitados

#Implementar `tiene_ciclo_no_dirigido(G)` que retorne `True` si el grafo no dirigido tiene al menos un ciclo.

def tiene_ciclo_no_dirigido(G):
    if len(G.nodes()) < 3:
        return False
    
    p = []
    visitados = set()
    inicio = list(G.nodes())[0]

    visitados.add(inicio)
    p.append(inicio)
    padres = {x: None for x in G.nodes}

    while p:
        v = p.pop()
        
        for w in G.neighbors(v):
            if w not in visitados:
                visitados.add(w)
                p.append(w)
                padres[w] = v
            elif w != padres[v]:
                return True
    return False

#Implementar `tiene_ciclo_dirigido(G)` para un Digrafo. Pista: usar estados (No visitado, Visitando, Visitado).

def tiene_ciclo_dirigido(G):
    estado = {x: 0 for x in G.nodes}
    inicio = list(G.nodes())[0]
    visitados = set()
    camino = set()

#Implementar `es_bipartito(G)` que verifique si un grafo no dirigido se puede colorear con 2 colores sin que dos nodos adyacentes tengan el mismo color.

def es_bipartito(G):
    q = [] 

    n = list(G.nodes())[0]

    color = {}
    color[n] = True
    q.append(n)

    while q:
        v = q.pop(n)

        for w in G.neighbors(v):
            if w not in color:
                color[w] = not color[v]
                q.append(w)
            else:
                if color[w] == color[v]:
                    return False

    return True

#Un grafo dirigido se considera bipartito si su **grafo subyacente** (el grafo no dirigido que resulta de quitar las direcciones) es bipartito.
#Implementar `es_digrafo_bipartito(DG)`.

def es_digrafo_bipartito(DG):
    return
#Implementar `orden_topologico_kahn(G)` que retorne una lista con el orden topológico de un DAG. Si el grafo tiene ciclos, retornar `None`.

import queue

def orden_topologico_kahn(G):
    q = deque()
    grado_entrada = {nodo: G.in_degree(nodo) for nodo in G.nodes}
    l = []
    for v in G.nodes:
        if grado_entrada[v] == 0:
            q.append(v)

    while q:
        v = q.popleft()
        l.append(v)

        for w in G.neighbors(v):
            grado_entrada[w] -= 1
            if grado_entrada[w] == 0:
                l.append(w)
    
    if len(l) != len(G.nodes):
        return None
    
    return l

#En un grafo bipartito de actores y películas, dos actores están a una **distancia de 0** si participaron en la misma película.

#1. Implementar `distancia_entre_actores(archivo_csv, actor_a, actor_b)` que retorne la distancia mínima entre dos actores (en grados de separación).  Si no hay camino entre dos actores o un actor no se encuentra en el archivo de datos devolver `None`.

#**Nota:** El archivo CSV tiene el formato `actor,pelicula`. Usar un grafo implícito, es decir, no cargar todo el grafo en memoria, sino que ir cargando nodos y aristas conforme se procesen.

def distancia_entre_actores(archivo_csv, actor_a, actor_b):
    return