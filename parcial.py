import csv
import json
# Se tiene el archivo recorridos.csv con información de los recorridos de colectivos que circulan por la Ciudad Autónoma de Buenos Aires.
# Escribir una función en Python que tome ese archivo y devuelva dos diccionarios, ida y vuelta, 
# donde las claves sean las localidades y los valores un conjunto de tuplas (linea, recorrido) con todas las líneas de colectivos que salen de esa localidad en el sentido indicado.
# Por ejemplo:

#	ida = {"LA BOCA": {(152, A,),(152, B), (152, C)}}
#	vuelta = {"OLIVOS": {(152, A), (152, C)}, "ESTACION BARTOLOME MITRE":{(152, B)}}


def obtener_recorridos(archivo_csv):
    with open(archivo_csv, "r", encoding="utf-8") as f:
        ida = {}
        vuelta = {}
        lector = csv.DictReader(f)
        for fila in lector:
            tupla_colectivo = (int(fila["linea"]), fila["recorrido"])
            localidad = fila["desde"]

            if fila["sentido"] == "IDA":
                if localidad not in ida:
                    ida[localidad] = {tupla_colectivo}
                else:
                    ida[localidad].add(tupla_colectivo)
            else:
                if localidad not in vuelta:
                    vuelta[localidad] = {tupla_colectivo}
                else:
                    vuelta[localidad].add(tupla_colectivo)
                    
    return ida, vuelta


def obtener_camino_minimo(G,s):
    distancias = {nodo: float("inf") for nodo in G}
    previo = {nodo: False for nodo in G}

    distancias[s] = 0

    for n in range(len(G)-1):
        for (u,v,d) in G.edges(data=True):
            peso = d["weight"]

            if distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                previo[v] = u

    for (u,v,d) in G.edfes(data=True):
        peso = d["weight"]

        if distancias[u] + peso < distancias[v]:
            print("Grafo con ciclo negativo")
            return None, None
    return distancias, previo
