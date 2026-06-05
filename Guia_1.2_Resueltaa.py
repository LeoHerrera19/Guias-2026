#Implementar `procesar_notas(notas)` que reciba una lista de notas (0-10) y retorne una lista solo con las notas de aprobación (>= 4) pero convertidas a "Aprobado". 
#Usar `map` y `filter`. No usar bucles `for`/`while`.

def procesar_notas(notas):
    notas_lambda = filter(lambda nota: nota >=4, notas)
    notas_final = map(lambda nota: "Aprobado", notas_lambda)
    return list(notas_final)

#Implementar `crear_multiplicador(n)` que retorne una función. Esa función retornada debe recibir un número `x` y devolver `x * n`.

def crear_multiplicador(n):
    def funcion(x):
        return x*n
    return funcion

#Implementar un decorador `logger` que antes de ejecutar la función imprima "Ejecutando funcion..." y después imprima "Terminado".

def logger(funcion):
    def suma(*args,**kwargs):
        print("Ejecutando funcion...")
        resultado = funcion(*args, **kwargs)
        print("Terminado")
        return resultado
    return suma
        
@logger
def suma(a, b):
    return a + b

#Implementar `division_segura(a, b)` que retorne el resultado de a/b. Si b es cero, retorna `None`. Si los argumentos no son números, retorna `None`.

def division_segura(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return None
    
    #Implementar `validar_edad(edad)`. Si la edad es negativa, levantar `ValueError` con el mensaje "Edad invalida". Si es valida, no hacer nada.

def validar_edad(edad):
    if edad < 0:
        raise ValueError("Edad invalida")
    return

#Implementar `contar_lineas(archivo)` que abra el archivo y retorne la cantidad de líneas. Asegurarse de cerrar el archivo (o usar with).

def contar_lineas(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        contenido = f.readlines()
    return len(contenido)

#Implementar `escribir_log(mensaje, archivo)` que agregue (append) el mensaje al final del archivo un salto de linea.

def escribir_log(mensaje, nombre_archivo):
    with open(nombre_archivo, "a", encoding="utf-8") as f:
        f.write(mensaje+ "\n")

#Implementar `leer_csv(archivo)` que lea un archivo CSV (sin cabecera) con formato `nombre,edad` y retorne una lista de diccionarios `[{'nombre': ..., 'edad': ...}]`.

import csv

def leer_csv(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        contenido = csv.DictReader(f, fieldnames=["nombre", "edad"])
        return list(contenido)

#Implementar `guardar_json(datos, archivo)` que tome un diccionario/lista y lo guarde en un archivo JSON.

import json

def guardar_json(datos, archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def guardar_json2(datos, archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        texto_json = json.dumps(datos, indent=4, ensure_ascii=False)
        f.write(texto_json)

#Implementar `inspeccionar(objeto)` que imprima el tipo del objeto y una lista de sus atributos públicos (que no empiezan con `_`). Usar `dir()`.

def inspeccionar(objeto):
    tipo = type(objeto)
    print(f"Tipo: {tipo}")

    lista = []
    for atributos in dir(objeto):
        if not atributos.startswith("_"):
            lista.append(atributos)
    
    print(f"Atributos públicos: {lista}")
    
