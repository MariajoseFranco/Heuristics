# Main
from reading_data import read_data
from constructivo import metodo_constructivo
from ruido import constructivo_con_ruido
from grasp import grasp1, grasp2
import time
import xlsxwriter



def Main():
    wb0 = xlsxwriter.Workbook('C:/Users/Asus/Desktop/constructivo_mariajose_franco_orozco.xlsx')
    wb1 = xlsxwriter.Workbook('C:/Users/Asus/Desktop/ruido_mariajose_franco_orozco.xlsx')
    wb2 = xlsxwriter.Workbook('C:/Users/Asus/Desktop/grasp1_mariajose_franco_orozco.xlsx')
    wb3 = xlsxwriter.Workbook('C:/Users/Asus/Desktop/grasp2_mariajose_franco_orozco.xlsx')

    datos = [
        'scp41.txt','scp42.txt','scpnrg1.txt','scpnrg2.txt',
        'scpnrg3.txt','scpnrg4.txt','scpnrg5.txt','scpnrh1.txt',
        'scpnrh2.txt','scpnrh3.txt','scpnrh4.txt','scpnrh5.txt'
    ]

    k = 3
    alpha = 0.05
    ruido = 5

    # CONSTRUCTIVO
    for dat in datos:
        archivo = open(dat)
        m, n, fo, restricciones = read_data(archivo)

        Z0, L0, S0, t0 = metodo_constructivo(m, n, fo, restricciones)
        print('C:\t',Z0,'\t',t0,'\t',dat)

        hoja0 = wb0.add_worksheet(dat)
        hoja0.write(0,0,Z0)
        hoja0.write(0,1,L0)
        q = 0
        for j in range(2,L0+2):
            hoja0.write(0,j,S0[q])
            q = q + 1
    wb0.close()

    # RUIDO
    for dat in datos:
        archivo = open(dat)
        m, n, fo, restricciones = read_data(archivo)

        Z1, L1, S1, t1 = constructivo_con_ruido(m, n, fo, restricciones, ruido)
        print('Ruido:\t',Z1,'\t',t1,'\t',dat)

        hoja1 = wb1.add_worksheet(dat)
        hoja1.write(0,0,Z1)
        hoja1.write(0,1,L1)
        q = 0
        for j in range(2,L1+2):
            hoja1.write(0,j,S1[q])
            q = q + 1
    wb1.close()

    # GRASP 1
    for dat in datos:
        archivo = open(dat)
        m, n, fo, restricciones = read_data(archivo)

        Z2, L2, S2, t2 = grasp1(m, n, fo, restricciones, k)
        print('GRASP 1:\t',Z2,'\t',t2,'\t',dat)

        hoja2 = wb2.add_worksheet(dat)
        hoja2.write(0,0,Z2)
        hoja2.write(0,1,L2)
        q = 0
        for j in range(2,L2+2):
            hoja2.write(0,j,S2[q])
            q = q + 1
    wb2.close()

    # GRASP 2
    for dat in datos:
        archivo = open(dat)
        m, n, fo, restricciones = read_data(archivo)

        Z3, L3, S3, t3 = grasp2(m, n, fo, restricciones, alpha)
        print('GRASP 2:\t',Z3,'\t',t3,'\t',dat)

        hoja3 = wb3.add_worksheet(dat)
        hoja3.write(0,0,Z3)
        hoja3.write(0,1,L3)
        q = 0
        for j in range(2,L3+2):
            hoja3.write(0,j,S3[q])
            q = q + 1
    wb3.close()

Main()