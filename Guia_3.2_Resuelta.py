

#Escribir un programa en Python que tome un archivo XML con un formato arbitrario y devuelva un archivo JSON donde cada una de las etiquetas del XML se convierte en una clave en JSON.

#Las etiquetas XML pueden tener atributos en ese caso debe preceder el nombre de la clave con `@` en el archivo json.

#Como las etiquetas se pueden repetir se debe usar una lista para almacenar el texto de las etiquetas.

import json
from pprint import pprint
from lxml import etree

def xml2json(xml_path):
    with open(xml_path, "r", encoding="utf-8") as f:
        contenido = f.read()
        resultado = {}
        