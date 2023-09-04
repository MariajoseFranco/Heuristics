# Algoritmo del metodo constructivo con ruido


from constructivo import metodo_constructivo_r
import random as r
import time

def constructivo_con_ruido(m, n, fo, restricciones, ruido):
    #se le agrega un ruido a los costos y se decide sobre estos nuevos costos, pero el valor obj se calcula con los costos anteriores
    t_inicial = time.time()
    fo_con_ruido = [0]*n
    for i in restricciones:
        for j in i:
            costos_con_ruido = fo[j-1] + r.randint(0,ruido) + r.random()
            if fo_con_ruido[j-1] == 0:
                fo_con_ruido[j-1] = costos_con_ruido
    vo, l, s, tc = metodo_constructivo_r(m, n, fo, restricciones, fo_con_ruido)

    t_final = time.time()
    t = t_final - t_inicial
    return vo, l, s, t