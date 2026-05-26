#Implementar `procesar_notas(notas)` que reciba una lista de notas (0-10) y retorne una lista solo con las notas de aprobación (>= 4) pero convertidas a "Aprobado". 
#Usar `map` y `filter`. No usar bucles `for`/`while`.

def procesar_notas(notas):
    notas_lambda = filter(lambda nota: nota >=4, notas)