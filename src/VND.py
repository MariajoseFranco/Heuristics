import time
from vecindarios import vecindario1, vecindario2, vecindario3

def vnd(vector_fo, matriz_restricciones, Z, L, S):
    t_inicial = time.time()
    Z_actual = Z
    S_actual = S
    j = 1
    while j <= 3:
        if j == 1:
            Z_nueva, S_nueva = vecindario1(vector_fo, matriz_restricciones, Z, L, S)
        elif j == 2:
            Z_nueva, S_nueva = vecindario2(vector_fo, matriz_restricciones, Z, L, S)
        elif j == 3:
            Z_nueva, S_nueva = vecindario3(vector_fo, matriz_restricciones, Z, L, S)

        if Z_nueva < Z_actual:
            j = 1
            Z_actual = Z_nueva
            S_actual = S_nueva
        else:
            j = j + 1
    t_final = time.time()
    t = t_final - t_inicial
    return Z_actual, len(S_actual), S_actual, t
