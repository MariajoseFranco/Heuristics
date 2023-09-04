# Algoritmo del metodo constructivo implementado
import math
import time


def metodo_constructivo(m, n, vector_fo, matriz_restricciones):
    t_inicial = time.time()
    #se hace la seleccion de los elementos
    seleccionados = list()
    for i in matriz_restricciones:
        primer_seleccionado = i[0]
        menor_costo = vector_fo[primer_seleccionado-1]
        tamaño = len(i)
        for j in range(1, tamaño):
            seleccionado_aux = i[j]
            costo_aux = vector_fo[seleccionado_aux-1]
            if menor_costo > costo_aux:
                menor_costo = costo_aux
                primer_seleccionado = seleccionado_aux
            elif menor_costo == costo_aux:
                cont_primer_seleccionado = 0
                cont_seleccionado_aux = 0
                for r in matriz_restricciones:
                    cont_primer_seleccionado = cont_primer_seleccionado + r.count(primer_seleccionado)
                    cont_seleccionado_aux = cont_seleccionado_aux + r.count(seleccionado_aux)
                    if cont_primer_seleccionado < cont_seleccionado_aux:
                        primer_seleccionado = seleccionado_aux
                        menor_costo = costo_aux
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

    #esto es para verificar que si se cumpla que cada restriccion es >= 1
    '''verif = list()
    for i in matriz_restricciones:
        for j in seleccionados:
            if j in i:
                verif.append(1)
                break
    print(len(verif))'''

    #esto es para hallar la cota inferior
    matriz_cubrimiento = list()
    suma_restricciones = list()
    for i in seleccionados:
        nodos_cubrimiento = list()
        for j in matriz_restricciones:
            if i in j:
                nodos_cubrimiento.append(1)
            else:
                nodos_cubrimiento.append(0)
            suma = sum(nodos_cubrimiento)
        matriz_cubrimiento.append(nodos_cubrimiento)
        suma_restricciones.append(suma)
    max_cubrimiento = max(suma_restricciones)
    nodos_min_necesarios = math.ceil(m/max_cubrimiento)

    cota_inferior = 0
    vector_fo_min = list()
    vfo = vector_fo[:]
    for i in range(0,nodos_min_necesarios):
        mini = min(vfo)
        vector_fo_min.append(mini)
        vfo.remove(mini)
        cota_inferior = cota_inferior + vector_fo_min[i]

    t_final = time.time()
    t = t_final - t_inicial
    return valor_objetivo, len(seleccionados), seleccionados, t


#Este metodo es igual que el de arriba solo que recibe un parametro mas y es el que se utiliza en del ruido
def metodo_constructivo_r(m, n, vector_fo, matriz_restricciones, fo_con_ruido):
    t_inicial = time.time()
    #se hace la seleccion de los elementos
    seleccionados = list()
    for i in matriz_restricciones:
        primer_seleccionado = i[0]
        menor_costo = fo_con_ruido[primer_seleccionado-1]
        tamaño = len(i)
        for j in range(1, tamaño):
            seleccionado_aux = i[j]
            costo_aux = fo_con_ruido[seleccionado_aux-1]
            if menor_costo > costo_aux:
                menor_costo = costo_aux
                primer_seleccionado = seleccionado_aux
            elif menor_costo == costo_aux:
                cont_primer_seleccionado = 0
                cont_seleccionado_aux = 0
                for r in matriz_restricciones:
                    cont_primer_seleccionado = cont_primer_seleccionado + r.count(primer_seleccionado)
                    cont_seleccionado_aux = cont_seleccionado_aux + r.count(seleccionado_aux)
                    if cont_primer_seleccionado < cont_seleccionado_aux:
                        primer_seleccionado = seleccionado_aux
                        menor_costo = costo_aux
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