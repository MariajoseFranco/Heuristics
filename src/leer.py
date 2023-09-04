from reading_data import read_data
from recocido_simulado import recocido_simulado

def leer():
    datos = [
        'scp41.txt','scp42.txt','scpnrg1.txt','scpnrg2.txt',
        'scpnrg3.txt','scpnrg4.txt','scpnrg5.txt','scpnrh1.txt',
        'scpnrh2.txt','scpnrh3.txt','scpnrh4.txt','scpnrh5.txt'
    ]

    k = 3
    alpha = 0.05
    ruido = 5
    Ti = 90
    Tf = 0.1
    c = 0.9
    Long = 10

    cp = list()
    file = open('sol1.txt')
    for line in file:
        a = line.split()
        cp.append(a)
    for dat in datos:
        archivo = open(dat)
        m, n, fo, restricciones = read_data(archivo)
        aux = 0
        for i in cp:
            Z0 = int(i[0])
            L0 = int(i[1])
            S = i[2:]
            S0 = [int(j) for j in S]
            print('C:\t',Z0)
            Z_mejorada, S_mejorada, tiempo = recocido_simulado(fo, restricciones, Ti, Tf, c, Long, Z0, L0, S0)
            print('C:\t',Z_mejorada)
            print('\n')
            aux = 1
            if aux == 1:
                break
        cp.pop(cp.index(i))

leer()