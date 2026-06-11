

# Crear un grafo no dirigido llamado `G` con 5 nodos (0 a 4) y las siguientes aristas: (0,1), (0,2), (1,2), (1,3), (2,4), (3,4). Luego, retornar el número de nodos y aristas.

import networkx as nx


def crear_grafo_basico():
    G = nx.Graph()
    G.add_edges_from([(0,1), (0,2), (1,2), (1,3), (2,4), (3,4)])
    nodos = G.number_of_nodes()
    aristas = G.number_of_edges()
    return nodos,aristas

#Implementar la función `crear_digrafo(aristas)` que reciba una lista de tuplas `(u, v)` y cree un grafo dirigido con esas aristas.

def crear_digrafo(aristas):
    G = nx.DiGraph()
    G.add_edges_from(aristas)
    return G

#Crear un grafo donde los nodos representen ciudades. Cada nodo debe tener un atributo `poblacion`. 
#Implementar `poblacion_total(G)` que sume las poblaciones de todos los nodos.

def poblacion_total(G):
    suma = 0
    for _,atributos in G.nodes(data='poblacion'):
        suma += atributos
    return suma

#Dada una lista de adyacencia (diccionario), construir manualmente la matriz de adyacencia como una lista de listas.

def dict_a_matriz(adj_dict):
    n = len(adj_dict)
    if n == 0:
        return []
    matriz = [[0] * n for _ in range(n)]
    for pos in adj_dict:
        for valor in adj_dict[pos]:
            matriz[pos][valor] = 1

    return matriz

#Implementar `matriz_a_lista_aristas(matriz)` que reciba una matriz de adyacencia y retorne una lista de tuplas `(u, v)` con las aristas presentes.

def matriz_a_lista_aristas(matriz):
    n = len(matriz)
    if n == 0:
        return []
    
    listas = []
    for pos in range(n):
        for valor in range(n):
            if matriz[pos][valor] == 1:
                listas.append((pos,valor))

    return listas


#Dada una red social (grafo dirigido), implementar una función que retorne el nodo con mayor número de seguidores (grado de entrada).

def mas_seguidores(G):
    nodo_inicial, grado_inicial = list(G.in_degree)[0]
  
    nodo = nodo_inicial
    popular = grado_inicial
  
    for nodito , grado in G.in_degree:
        if grado > popular:
            popular = grado
            nodo = nodito
  
    return nodo

def mas_seguidores1(G):
    return max(G.in_degree, key=lambda x: x[1])[0]

#Implementar `distribucion_grados(G)` que retorne un diccionario donde las claves sean los grados y los valores la cantidad de nodos con ese grado.

def distribucion_grados(G):
    grados = {}
    for _, grado in G.in_degree:
        if grado not in grados:
            grados[grado] = 1
        else:
            grados[grado] +=1
    return grados

#Modelar una red de transporte con 3 estaciones (A, B, C) y rutas: A->B (10 min), B->C (15 min), A->C (20 min).
#Implementar `tiempo_ruta(G, nodo1, nodo2)` que retorne el tiempo de la arista.

def crear_red_transporte():
    G = nx.DiGraph()
    G.add_weighted_edges_from(("A","B",10),("B","C",15),("A","c",20))
    return G


def tiempo_ruta(G, u, v):
    return G[u][v]["weight"]

#En una red social, 'seguir' es dirigido y 'ser amigo' es no dirigido.
#Implementar `convertir_a_amistades(G_seguidores)` que transforme un Digrafo de seguidores en un Grafo de amistades donde existe una arista si y solo si se siguen mutuamente.

def convertir_a_amistades(G_seguidores):
    G_amigs = nx.Graph()
    for nodo, vecino in G_seguidores.edges:
        if G_seguidores.has_edge(vecino,nodo):
            G_amigs.add_edge(nodo,vecino)

    return G_amigs