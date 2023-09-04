import random as r
from ruido import constructivo_con_ruido
from recocido_simulado import recocido_simulado
import time


def algoritmo_genetico(generaciones, num_hijos, prob_mutacion, m, n, vector_fo, matriz_restricciones, Ti, Tf, c, Long):
    pob_inicial_S = list()
    pob_inicial_Z = list()
    for i in range(100):
        ruido = r.randint(0,9)
        Z, L, S, t = constructivo_con_ruido(m, n, vector_fo, matriz_restricciones, ruido)
        pob_inicial_S.append(S)
        pob_inicial_Z.append(Z)

    t_inicial = time.time()
    for i in range(generaciones):
        hZ = list()
        hS = list()
        for j in range(num_hijos):
            padreZ, padreS, madreZ, madreS = seleccion(pob_inicial_Z, pob_inicial_S)
            hijoZ, hijoS = cruce(padreS, madreS, vector_fo)
            if r.random() <= prob_mutacion:
                hijoZ, hijoS = mutacion(hijoS, vector_fo, matriz_restricciones)
            hijoZ_factible, L_mejorada, hijoS_factible, tiempo = recocido_simulado(vector_fo, matriz_restricciones, Ti, Tf, c, Long, hijoZ, len(hijoS), hijoS)
            hZ.append(hijoZ_factible)
            hS.append(hijoS_factible)
            t0 = time.time() - t_inicial
            if t0 >= 200:
                break
        pob_inicial_Z, pob_inicial_S = actualizacion(pob_inicial_Z, pob_inicial_S, hZ, hS)
    mejor_solucion_Z = min(pob_inicial_Z)
    index_mejor_solucion = pob_inicial_Z.index(mejor_solucion_Z)
    mejor_solucion_S = pob_inicial_S[index_mejor_solucion]
    t_final = time.time()
    t = t_final - t_inicial
    return mejor_solucion_Z, mejor_solucion_S, t


# Seleccion por ruleta
def seleccion(pob_inicial_Z, pob_inicial_S):
    pob_aux = list()
    probabilidades = list()
    for i in pob_inicial_Z:
        div = 1/i
        pob_aux.append(div)
    total = sum(pob_aux)
    for j in pob_aux:
        probabilidad = j/total
        probabilidades.append(probabilidad)
    s1 = 10000
    s2 = 10000
    a = min(probabilidades)
    b = max(probabilidades)
    aleatorio1 = r.random()*(b-a)+a
    aleatorio2 = r.random()*(b-a)+a
    for k in probabilidades:
        if s1 != 10000 and s2 != 10000:
            break
        else:
            if s1 == 10000:
                if k >= aleatorio1:
                    s1 = probabilidades.index(k)
            if s2 == 10000:
                if probabilidades.index(k) != s1:
                    if k >= aleatorio2:
                        s2 = probabilidades.index(k)
    if s1 == 10000 and s2 != 10000:
        for k in range(len(probabilidades)):
            if k != s2:
                s1 = k
    if s1 != 10000 and s2 == 10000:
        for k in range(len(probabilidades)):
            if k != s1:
                s2 = k
    if s1 == 10000 and s2 == 10000:
        s1 = 0
        s2 = 1

    padre_Z = pob_inicial_Z[s1]
    padre_S = pob_inicial_S[s1]
    madre_Z = pob_inicial_Z[s2]
    madre_S = pob_inicial_S[s2]
    return padre_Z, padre_S, madre_Z, madre_S


# Cruce por un punto
def cruce(padre_S, madre_S, vector_fo):
    aleatorio = r.randint(0, len(padre_S))
    particion1_S = padre_S[0:aleatorio]
    particion2_S = madre_S[aleatorio:len(madre_S)]
    hijo_S = particion1_S + particion2_S
    valor_objetivo = 0
    for j in hijo_S:
        costo_seleccionados = vector_fo[j-1]
        valor_objetivo = valor_objetivo + costo_seleccionados
    return valor_objetivo, hijo_S


# Mutacion de un gen aleatoriamente
def mutacion(hijo_S, vector_fo, matriz_restricciones):
    aleatorio = r.randint(0, len(hijo_S)-1)
    for i in matriz_restricciones:
        elegido = i[0]
        if elegido not in hijo_S:
            hijo_S[aleatorio] = elegido
            break
    hijo_S.sort()
    valor_objetivo = 0
    for j in hijo_S:
        costo_seleccionados = vector_fo[j-1]
        valor_objetivo = valor_objetivo + costo_seleccionados
    return valor_objetivo, hijo_S


def actualizacion(pob_inicial_Z, pob_inicial_S, hZ, hS):
    for i in range(0, len(hZ)):
        peor_solucion = max(pob_inicial_Z)
        index_peor_solucion = pob_inicial_Z.index(peor_solucion)
        pob_inicial_Z[index_peor_solucion] = hZ[i]
        pob_inicial_S[index_peor_solucion] = hS[i]
    return pob_inicial_Z, pob_inicial_S

