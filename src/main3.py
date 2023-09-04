from reading_data import read_data
from algoritmo_genetico import algoritmo_genetico
import xlsxwriter

def Main():
    wb0 = xlsxwriter.Workbook('C:/Users/Asus/Desktop/GA_mariajose_franco_orozco.xlsx')

    datos = [
        'scp41.txt','scp42.txt','scpnrg1.txt','scpnrg2.txt',
        'scpnrg3.txt','scpnrg4.txt','scpnrg5.txt','scpnrh1.txt',
        'scpnrh2.txt','scpnrh3.txt','scpnrh4.txt','scpnrh5.txt'
    ]
    #datos = ['scp41.txt','scp42.txt']

    Ti = 90
    Tf = 0.1
    c = 0.9
    Long = 10
    generaciones = 10
    num_hijos = 5
    prob_mutacion = 0.4


    for dat in datos:
        archivo = open(dat)
        m, n, fo, restricciones = read_data(archivo)
        Z, S, t = algoritmo_genetico(generaciones, num_hijos, prob_mutacion, m, n, fo, restricciones, Ti, Tf, c, Long)
        print('GA:\t',Z,'\t',t,'\t',dat)

        L = len(S)
        hoja0 = wb0.add_worksheet(dat)
        hoja0.write(0,0,Z)
        hoja0.write(0,1,L)
        q = 0
        for j in range(2,L+2):
            hoja0.write(0,j,S[q])
            q = q + 1
    wb0.close()

Main()