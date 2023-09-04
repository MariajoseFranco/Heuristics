from reading_data import read_data
from recocido_simulado import recocido_simulado
from vecindarios import vecindario1, vecindario2, vecindario3, factibilidad
from VND import vnd
import time
import xlsxwriter

def Main():
    wb0 = xlsxwriter.Workbook('C:/Users/Asus/Desktop/constructivo_mariajose_franco_orozco.xlsx')

    datos = [
        'scp41.txt','scp42.txt','scpnrg1.txt','scpnrg2.txt',
        'scpnrg3.txt','scpnrg4.txt','scpnrg5.txt','scpnrh1.txt',
        'scpnrh2.txt','scpnrh3.txt','scpnrh4.txt','scpnrh5.txt'
    ]

    Ti = 90
    Tf = 0.1
    c = 0.9
    Long = 10

    # LEER DATOS
    cp = list()
    file = open('sol1.txt')
    for line in file:
        a = line.split()
        cp.append(a)
    for dat in datos:
        archivo = open(dat)
        m, n, fo, restricciones = read_data(archivo)
        aux = 0
        hoja0 = wb0.add_worksheet(dat)
        for i in cp:
            Z0 = int(i[0])
            L0 = int(i[1])
            S = i[2:]
            S0 = [int(j) for j in S]
            print('Solución inicial:\t',Z0,'\t',dat)
            hoja0.write(0,0,Z0)
            hoja0.write(0,1,L0)
            q = 0
            for j in range(2,L0+2):
                hoja0.write(0,j,S0[q])
                q = q + 1

            # RECOCIDO SIMULADO
            Z_mejorada1, L_mejorada1, S_mejorada1, tiempo1 = recocido_simulado(fo, restricciones, Ti, Tf, c, Long, Z0, L0, S0)
            print('Recocido Simulado:\t',Z_mejorada1,'\t', tiempo1)
            hoja0.write(1,0,Z_mejorada1)
            hoja0.write(1,1,L_mejorada1)
            q = 0
            for j in range(2,L_mejorada1+2):
                hoja0.write(1,j,S_mejorada1[q])
                q = q + 1

            # # VND
            Z_mejorada2, L_mejorada2, S_mejorada2, tiempo2 = vnd(fo, restricciones, Z0, L0, S0)
            print('VND:\t',Z_mejorada2,'\t', tiempo2)
            print('\n')
            hoja0.write(2,0,Z_mejorada2)
            hoja0.write(2,1,L_mejorada2)
            q = 0
            for j in range(2,L_mejorada2+2):
                hoja0.write(2,j,S_mejorada2[q])
                q = q + 1
            aux = 1
            if aux == 1:
                break
        cp.pop(cp.index(i))
    wb0.close()

Main()