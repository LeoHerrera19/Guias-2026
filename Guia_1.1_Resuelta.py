#Implementar la función `contar_vocales(texto)`. Esta función debe recibir una cadena de texto (string) y retornar un diccionario
#donde las claves sean las vocales (a, e, i, o, u) y los valores sean la cantidad de veces que cada vocal aparece en el texto.
#La cuenta debe ser insensible a mayúsculas y minúsculas (es decir, 'A' y 'a' se cuentan como la misma vocal). 
#Si una vocal no se encuentra en el texto, su valor en el diccionario debe ser 0.

def contar_vocales(texto):
    vocales = { "a" : 0, "e":0,"i":0,"o":0,"u":0}
   
    for letra in texto:
            letra_m = letra.lower()
            if letra_m in vocales:
                  vocales[letra_m] +=1
    return vocales


resultado = contar_vocales("Hola Mundo")
assert resultado.get("a", 0) == 1
assert resultado.get("o", 0) == 2
assert resultado.get("u", 0) == 1
assert resultado.get("e", 0) == 0
assert resultado.get("i", 0) == 0

resultado_complejo = contar_vocales("Murcielago")
assert resultado_complejo["a"] == 1
assert resultado_complejo["e"] == 1
assert resultado_complejo["i"] == 1
assert resultado_complejo["o"] == 1
assert resultado_complejo["u"] == 1
assert contar_vocales("") == {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

# Cadena sin vocales
assert contar_vocales("Rhythm") == {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
assert contar_vocales("bcdfg") == {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

# Cadena con solo vocales (mayúsculas y minúsculas)
resultado_solo_vocales = contar_vocales("AEIOUaeiou")
assert resultado_solo_vocales["a"] == 2
assert resultado_solo_vocales["e"] == 2
assert resultado_solo_vocales["i"] == 2
assert resultado_solo_vocales["o"] == 2
assert resultado_solo_vocales["u"] == 2

# Cadena con caracteres especiales y números
resultado_especiales = contar_vocales("123!@#aEIOU")
assert resultado_especiales["a"] == 1
assert resultado_especiales["e"] == 1
assert resultado_especiales["i"] == 1
assert resultado_especiales["o"] == 1
assert resultado_especiales["u"] == 1

# Cadena con una sola vocal repetida
resultado_solo_a = contar_vocales("AAAAA")
assert resultado_solo_a["a"] == 5
assert resultado_solo_a["e"] == 0
assert resultado_solo_a["i"] == 0
assert resultado_solo_a["o"] == 0
assert resultado_solo_a["u"] == 0

# Ejercicio 1: Tests pasados!

#Implementar la función `es_palindromo(texto)` que verifique si un string es un palíndromo (se lee igual de izquierda a derecha).
#Debe ignorar espacios y no distinguir entre mayúsculas y minúsculas.

def es_palindromo(texto):
    minus = texto.lower()
    texto_limpio = ""
    for letra in minus:
          if letra != " ":
                texto_limpio += letra

    return texto_limpio == texto_limpio[::-1]
    

assert es_palindromo("Neuquen") == True
assert es_palindromo("Anita lava la tina") == True
assert es_palindromo("Hola") == False
assert es_palindromo("") == True

# Ejercicio 2: Tests pasados!

#Implementar la función `filtrar_pares(numeros)` que reciba una lista de enteros y retorne una lista conteniendo solo los números pares.

def filtrar_pares(numeros):
    lista_pares = [x for x in numeros if x % 2 != 0]
    return lista_pares
    
# Tests
assert filtrar_pares([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
assert filtrar_pares([1, 3, 5]) == []
assert filtrar_pares([2, 4, 6]) == [2, 4, 6]
assert filtrar_pares([]) == []

# Ejercicio 3: Tests pasados!

#Implementar `cuadrados_impares(numeros)` que reciba una lista de números y retorne una lista con los cuadrados de los números impares,
#utilizando **List Comprehensions**.

def cuadrados_impares(numeros):
    lista_cuadrados = [x**2 for x in numeros if x % 2 != 0]
    return lista_cuadrados

assert cuadrados_impares([1, 2, 3, 4, 5]) == [1, 9, 25]
assert cuadrados_impares([2, 4, 6]) == []
assert cuadrados_impares([0, 1]) == [1]

# Ejercicio 4: Tests pasados!

#Implementar `elementos_comunes(lista1, lista2)` que retorne un `set` con los elementos que aparecen en ambas listas.

def elementos_comunes(lista1, lista2):
     return set(lista1) & set(lista2)

#Implementar `min_max_tupla(numeros)` que reciba una lista de números y retorne una tupla `(minimo, maximo)`.
#  Si la lista está vacía debe retornar una tupla con dos valores `None`.

def min_max_tupla(numeros):
    if len(numeros) == 0:
         return (None, None)
    min = numeros[0]
    max = numeros[0]

    for n in numeros:
        if max < n:
             max = n
        if n< min:
             min = n
    return (min,max)

#Implementar `factorial(n)` que calcule el factorial de un número de manera iterativa (no recursiva). Usar técnicas de programación dinámica para optimizar el cálculo.

def factorial(n):
    lista = [1, 1]

    for num in range(2,n+1):
        lista.append(num*lista[num-1])
    
    return lista[-1]
    
#Implementar `calculadora_basica(operacion, *args)` que realice una operación ('suma', 'resta', 'multiplicacion') sobre todos los argumentos pasados.
#*   'suma': sumar todos
#*   'resta': restar al primero el resto
#*   'multiplicacion': multiplicar todos

def calculadora_basica(operacion, *args):
    resultado = args[0]
    for numero in args[1:]:
        if operacion == "suma":
            resultado += numero
            
        elif operacion == "resta":
            resultado -= numero
            
        elif operacion == "multiplicacion":
            resultado *= numero
    return resultado
    
#Implementar `formatear_saludo(mensaje, **kwargs)` que tome un mensaje base con placeholders (ej: "Hola {nombre}")
#  y reemplace los valores usando los argumentos nombrados.

def formatear_saludo(mensaje, **kwargs):
    return mensaje.format(**kwargs)

#Implementar `validar_contrasena(password)` que verifique si una contraseña es válida.
#Reglas:
#*   Longitud mayor a 8
#*   Debe contener al menos un numero
#*   Debe contener al menos una mayúscula

def validar_contrasena(password):
    if len(password)<=8 :
         return False
    
    num = False
    letra = False

    for i in password:
        if i.isdigit():
              num = True
        if i.isupper():
            letra = True

    if num == False:
        return num
    if letra == False:
         return letra
    return num and letra

