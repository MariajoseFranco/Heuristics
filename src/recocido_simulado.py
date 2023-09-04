import time
from vecindarios import vecindario1
import random
import numpy as np

def recocido_simulado(vector_fo, matriz_restricciones, Ti, Tf, c, Long, Z, L, S):
    t_inicial = time.time()
    Z_actual = Z
    S_actual = S
    temperatura = Ti
    t1 = time.time()
    while temperatura > Tf:
        for i in range(1,Long):
            Z_nueva, S_nueva = vecindario1(vector_fo, matriz_restricciones, Z, L, S) #aqui es donde debo tener en cuenta L
            if Z_nueva < Z_actual:
                Z_actual = Z_nueva
                S_actual = S_nueva
            else:
                r = random.uniform(0.0, 1.0)
                if r < np.exp((Z_actual-Z_nueva)/temperatura):
                    Z_actual = Z_nueva
                    S_actual = S_nueva
            t0 = time.time() - t1
            if t0 >= 10:
                break
        if t0 >= 30:
                break
        temperatura = c*temperatura
    t_final = time.time()
    t = t_final - t_inicial
    return Z_actual, len(S_actual), S_actual, t