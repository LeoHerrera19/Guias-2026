

#Implementar el algoritmo de Dijkstra para encontrar la distancia mínima desde un origen `s` a todos los demás nodos. Utilizar `heapq` para la cola de prioridad.

import heapq
import networkx as nx


def dijkstra_manual(G, s):
    # G es un nx.Graph o nx.DiGraph con pesos en las aristas ('weight')
    # Tu código aquí
    distancias = {nodo: float("inf") for nodo in G.nodes}
    distancias[s] = 0
    previos = {n : None for n in G.nodes}
    visitados = {n : False for n in G.nodes}
    pq = [(0, s)]

    while pq:
        dista, v = heapq.heappop(pq)
        if visitados[v]:
            continue
        visitados[v] = True

        for w in G.neighbors(v):
            if not visitados[w]:
                if distancias[v] + G[v][w]["weight"] < distancias[w]:
                    distancias[w] = distancias[v] + G[v][w]["weight"]
                    previos[w] = v
                    heapq.heappush(pq,(distancias[w],w))
    return distancias

#Modificar la implementación anterior para que `dijkstra_camino(G, s, t)` retorne una lista con los nodos del camino mínimo entre `s` y `t`.

def dijkstra_camino(G, s, t):
    
    distancias = {nodo: float("inf") for nodo in G.nodes}
    distancias[s] = 0
    previos = {n : None for n in G.nodes}
    visitados = {n : False for n in G.nodes}
    pq = [(0, s)]
    
    while pq:
        dista, v = heapq.heappop(pq)
        if v == t:
            break
        if visitados[v]:
            continue
        visitados[v] = True
        for w in G.neighbors(v):
            if not visitados[w]:
                if distancias[v] + G[v][w]["weight"] < distancias[w]:
                    distancias[w] = distancias[v] + G[v][w]["weight"]
                    previos[w] = v
                    heapq.heappush(pq, (distancias[w], w))
    if distancias[t] == float("inf"):
        return None
        
    caminos = []
    nodo_actual = t

    while nodo_actual is not None:
        caminos.append(nodo_actual)
        nodo_actual = previos[nodo_actual]

    return caminos[::-1]

#Demostrar que Dijkstra puede fallar con aristas negativas. 
#Crear un grafo con una arista negativa donde `nx.dijkstra_path` y `nx.bellman_ford_path` den resultados diferentes.

def crear_grafo_arista_negativa():
    G = nx.DiGraph()
    G.add_weighted_edges_from([(0,1,2),(1,2,5),(2,3,-10),(1,3,4)])
    return G


def comparar_algoritmos():
    G = crear_grafo_arista_negativa()
    camino_dijkstra = nx.dijkstra_path(G, source=0, target=3)
    camino_bellman = nx.bellman_ford_path(G, source=0, target=3)
    return camino_dijkstra, camino_bellman

#Implementar `bellman_ford_manual(G, s)` que retorne las distancias mínimas o lance una excepción si detecta un ciclo negativo.

def bellman_ford_manual(G, s):
    
    distancias = {n: float("inf") for n in G.nodes}
    previo = {n: None for n in G.nodes}
    distancias[s] = 0

    for _ in range(len(G.nodes)-1):
        for (v,w,peso) in G.edges(data="weight"):
            if distancias[v] + peso < distancias[w]:
                distancias[w] = distancias[v] + peso
                previo[w] = v
        
    for (v,w,peso) in G.edges(data="weight"):
            if distancias[v] + peso < distancias[w]:
                raise ValueError("Grafo con nodos negativos")
                
    return distancias

#Implementar `tiene_ciclo_negativo(G)` utilizando el algoritmo de Bellman-Ford.

def tiene_ciclo_negativo(G):

    distancias = {n: float("inf") for n in G.nodes}
    previo = {n: None for n in G.nodes}
    inicio = list(G.nodes())[0]
    distancias[inicio] = 0

    for _ in range(len(G.nodes)-1):
        for (v,w,peso) in G.edges(data="weight"):
            if distancias[v] + peso < distancias[w]:
                distancias[w] = distancias[v] + peso
                previo[w] = v
        
    for (v,w,peso) in G.edges(data="weight"):
            if distancias[v] + peso < distancias[w]:
                return True
                
    return False

#Un camión debe ir del punto A al B pasando por un conjunto de ciudades. Cada arista tiene un costo (combustible). 
#Implementar `ruta_economica(G, origen, destino)`.

import heapq
def ruta_economica(G, origen, destino):
   
    distancias = {n: float("inf") for n in G.nodes}
    distancias[origen] = 0
    previo = {n: None for n in G.nodes}
    visitados = {n: False for n in G.nodes}
    pq = [(0,origen)]

    while pq:
        distanciav , v = heapq.heappop(pq)
        if v == destino:
            break
        if visitados[v]:
            continue
        visitados[v] = True
        for w in G.neighbors(v):
            if not visitados[w]:
                if distancias[v] + G[v][w]["weight"] < distancias[w]:
                    distancias[w] = distancias[v] + G[v][w]["weight"]
                    previo[w] = v
                    heapq.heappush(pq,(distancias[w], w))
    if distancias[destino] == float("inf"):
        return None
        
    caminos = []
    nodo_actual = destino

    while nodo_actual is not None:
        caminos.append(nodo_actual)
        nodo_actual = previo[nodo_actual]

    return caminos[::-1]

#En una red de computadoras, se busca el camino con menor latencia total. 
#Si se encuentran dos caminos con igual latencia, se prefiere el que tenga menos saltos (aristas).
#Implementar `mejor_camino_red(G, s, t)`.

def mejor_camino_red(G, s, t):

    distancias = {n: float("inf") for n in G.nodes}
    visitados = {n: False for n in G.nodes}
    previo = {n: None for n in G.nodes}
    distancias[s] = 0
    saltos = {n: float("inf") for n in G.nodes}
    saltos[s] = 0
    pq = [(0,0,s)]

    while pq:
        latenciav ,saltosv, v = heapq.heappop(pq)

        if v == t:
            break

        if visitados[v]:
            continue
        visitados[v] = True

        for w in G.neighbors(v):
            if not visitados[w]:
                nueva_latencia =distancias[v] + G[v][w]["weight"]
                nuevos_saltos = saltos[v]+1
                if (nueva_latencia < distancias[w]) or (nueva_latencia == distancias[w] and nuevos_saltos < saltos[w]):
                    distancias[w] = nueva_latencia
                    saltos[w] = nuevos_saltos
                    previo[w] = v
                    heapq.heappush(pq, (distancias[w],saltos[w], w))
    
    if distancias[t] == float("inf"):
        return None
    
    camino = []
    nodo_actual = t
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual= previo[nodo_actual]

    return camino[::-1]
