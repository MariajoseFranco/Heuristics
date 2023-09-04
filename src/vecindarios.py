import time
import random as r

##################################################### VECINDARIOS #####################################################

# Formar el vecindario 1
def vecindario1(vector_fo, matriz_restricciones, Z, L, S): # Sacarle 1 elemento a la lista de seleccionados
    t_inicial = time.time()
    S_n = list()
    Z_n = list()
    t1 = time.time()
    for i in range(0, L):
        S_reformada = S[:]
        S_reformada.pop(i)
        valor_objetivo = 0
        for j in S_reformada:
            costo_seleccionados = vector_fo[j-1]
            valor_objetivo = valor_objetivo + costo_seleccionados
        Z_n.append(valor_objetivo)
        S_n.append(S_reformada)
        t0 = time.time() - t1
        if t0 >= 120:
            break
    Z_acep, S_acep = factibilidad(vector_fo, matriz_restricciones, Z_n, S_n)
    pos = r.randint(0, len(Z_acep)-1)
    Z_mejorada = Z_acep[pos]
    S_mejorada = S_acep[pos]
    t_final = time.time()
    t = t_final - t_inicial
    return Z_mejorada, S_mejorada

# Formar el vecindario 2
def vecindario2(vector_fo, matriz_restricciones, Z, L, S): # Sacarle 2 elemento a la lista de seleccionados
    t_inicial = time.time()
    S_n = list()
    Z_n = list()
    t1 = time.time()
    for i in range(0, L):
        for j in range(0, L):
            S_reformada = S[:]
            if i != j:
                if i > j:
                    S_reformada.pop(i)
                    S_reformada.pop(j)
                else:
                    S_reformada.pop(j)
                    S_reformada.pop(i)
                valor_objetivo = 0
                for k in S_reformada:
                    costo_seleccionados = vector_fo[k-1]
                    valor_objetivo = valor_objetivo + costo_seleccionados
                Z_n.append(valor_objetivo)
                S_n.append(S_reformada)
                t0 = time.time() - t1
                if t0 >= 30:
                    break
        if t0 >= 30:
            break
    Z_acep, S_acep = factibilidad(matriz_restricciones, Z_n, S_n)
    pos = r.randint(0, len(Z_acep)-1)
    Z_mejorada = Z_acep[pos]
    S_mejorada = S_acep[pos]
    t_final = time.time()
    t = t_final - t_inicial
    return Z_mejorada, S_mejorada

# Formar el vecindario 3
def vecindario3(vector_fo, matriz_restricciones, Z, L, S): # Sacarle 1 elemento a la lista de seleccionados y meter 1 que no estaba
    t_inicial = time.time()
    S_n = list()
    Z_n = list()
    t1 = time.time()
    for i in range(0, L):
        S_reformada = S[:]
        elemento = S_reformada[i]
        S_reformada.pop(i)
        for k in range(1, len(vector_fo)+1):
            nuevo_elemento = k
            if (nuevo_elemento != elemento) and (nuevo_elemento not in S_reformada):
                break
        S_reformada.append(nuevo_elemento)
        S_reformada.sort()
        valor_objetivo = 0
        for j in S_reformada:
            costo_seleccionados = vector_fo[j-1]
            valor_objetivo = valor_objetivo + costo_seleccionados
        Z_n.append(valor_objetivo)
        S_n.append(S_reformada)
        t0 = time.time() - t1
        if t0 >= 30:
            break
    Z_acep, S_acep = factibilidad(matriz_restricciones, Z_n, S_n)
    pos = r.randint(0, len(Z_acep)-1)
    Z_mejorada = Z_acep[pos]
    S_mejorada = S_acep[pos]
    t_final = time.time()
    t = t_final - t_inicial
    return Z_mejorada, S_mejorada

##################################################### FACTIBILIDAD #####################################################

# Para formar un vecindario de unicamente los vecinos factibles
def factibilidad(vector_fo, matriz_restricciones, Z, S):
    t_inicial = time.time()
    Z_aceptada = list()
    S_aceptada = list()
    S = list()
    t1 = time.time()
    for o in S:
        verif = list()
        aleat = r.randint(0, len(S)-1)
        k = S[aleat]
        pos = S.index(k)
        for i in matriz_restricciones:
            for j in k:
                if j in i:
                    verif.append(1)
                    break
        if len(verif) == len(matriz_restricciones):
            S_aceptada.append(k)
            Z_aceptada.append(Z[pos])
        t0 = time.time() - t1
        if t0 >= 60:
            break
    # Si no hay vecindarios factibles
    if Z_aceptada == []:
        for i in matriz_restricciones:
            elegido = i[0]
            S.append(elegido)

        #se verifica si hay seleccionados repetidos y se eliminan los repetidos
        longitud = len(S)
        k = 0
        for i in range(0,longitud):
            if S.count(S[k]) > 1:
                S.pop(k)
                k = k-1
            k = k+1
        S.sort()

        #se halla el costo de haber seleccionado los que se seleccionaron (valor objetivo)
        valor_objetivo = 0
        for j in S:
            costo_seleccionados = vector_fo[j-1]
            valor_objetivo = valor_objetivo + costo_seleccionados
        Z_aceptada.append(valor_objetivo)
        S_aceptada.append(S)

    t_final = time.time()
    t = t_final - t_inicial
    return Z_aceptada, S_aceptada