# Algoritmo del metodo GRASP
import random as r
import math
import time


#GRASP basado en cardinalidad
def grasp1(m, n, vector_fo, matriz_restricciones, k):
    t_inicial = time.time()
    #se hace la seleccion de los elementos
    seleccionados = list()
    for i in matriz_restricciones:
        rcl = list()
        tamaño = len(i)
        if tamaño <= k:
            for j in range(0, tamaño):
                seleccionado_iteraciones = i[j]
                rcl.append(seleccionado_iteraciones)
        else:
            lista_aux = i[:]
            for d in range(0, k):
                seleccionado_iteraciones = min(lista_aux)
                rcl.append(seleccionado_iteraciones)
                lista_aux.remove(seleccionado_iteraciones)
        aleatorio = r.randint(0,len(rcl)-1)
        primer_seleccionado = rcl[aleatorio]
        seleccionados.append(primer_seleccionado)

    #se verifica si hay seleccionados repetidos y se eliminan los repetidos
    longitud = len(seleccionados)
    c = 0
    for i in range(0,longitud):
        if seleccionados.count(seleccionados[c]) > 1:
            seleccionados.pop(c)
            c = c-1
        c = c+1
    seleccionados.sort()

    #se halla el costo de haber seleccionado los que se seleccionaron (valor objetivo)
    valor_objetivo = 0
    for j in seleccionados:
        costo_seleccionados = vector_fo[j-1]
        valor_objetivo = valor_objetivo + costo_seleccionados

    t_final = time.time()
    t = t_final - t_inicial
    return valor_objetivo, len(seleccionados), seleccionados, t



#GRASP basado en valor
def grasp2(m, n, vector_fo, matriz_restricciones, alpha):
    t_inicial = time.time()
    #se hace la seleccion de los elementos
    seleccionados = list()
    for i in matriz_restricciones:
        elegibles = list()
        costos_elegibles = list()
        rcl = list()
        tamaño = len(i)
        for j in range(0, tamaño):
            seleccionado_iteraciones = i[j]
            elegibles.append(seleccionado_iteraciones)
            costo_iteraciones = vector_fo[seleccionado_iteraciones-1]
            costos_elegibles.append(costo_iteraciones)
        max_elegible = max(costos_elegibles)
        min_elegible = min(costos_elegibles)
        l = len(costos_elegibles)
        for k in range(0,l):
            if costos_elegibles[k] <= alpha*(max_elegible - min_elegible) + min_elegible:
                rcl.append(elegibles[k])
        aleatorio = r.randint(0,len(rcl)-1)
        primer_seleccionado = rcl[aleatorio]
        seleccionados.append(primer_seleccionado)

    #se verifica si hay seleccionados repetidos y se eliminan los repetidos
    longitud = len(seleccionados)
    k = 0
    for i in range(0,longitud):
        if seleccionados.count(seleccionados[k]) > 1:
            seleccionados.pop(k)
            k = k-1
        k = k+1
    seleccionados.sort()

    #se halla el costo de haber seleccionado los que se seleccionaron (valor objetivo)
    valor_objetivo = 0
    for j in seleccionados:
        costo_seleccionados = vector_fo[j-1]
        valor_objetivo = valor_objetivo + costo_seleccionados

    t_final = time.time()
    t = t_final - t_inicial
    return valor_objetivo, len(seleccionados), seleccionados, t