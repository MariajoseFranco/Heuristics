# Main
from reading_data import read_data
from constructivo import metodo_constructivo
from ruido import constructivo_con_ruido
from grasp import grasp1, grasp2
import time
import xlsxwriter

def Main():
    workbook = xlsxwriter.Workbook('constructivo_mariajose_franco_orozco.xlsx')
    worksheet = workbook.add_worksheet('scp41')
    worksheet = workbook.add_worksheet('scp42')
    worksheet = workbook.add_worksheet('scpnrg1')
    worksheet = workbook.add_worksheet('scpnrg2')
    worksheet = workbook.add_worksheet('scpnrg3')
    worksheet = workbook.add_worksheet('scpnrg4')
    worksheet = workbook.add_worksheet('scpnrg5')
    worksheet = workbook.add_worksheet('scpnrh1')
    worksheet = workbook.add_worksheet('scpnrh2')
    worksheet = workbook.add_worksheet('scpnrh3')
    worksheet = workbook.add_worksheet('scpnrh4')
    worksheet = workbook.add_worksheet('scpnrh5')

    t_inicial = time.time()
    print('0 - prueba.txt\n1 - scp41.txt\n2 - scp42.txt\n3 - scpnrg1.txt\n4 - scpnrg2.txt\n5 - scpnrg3.txt\n6 - scpnrg4.txt\n7 - scpnrg5.txt\n8 - scpnrh1.txt\n9 - scpnrh2.txt\n10 - scpnrh3.txt\n11 - scpnrh4.txt\n12 - scpnrh5.txt')
    data = input("Ingrese el numero del archivo que desea evaluar:")

    if data == '1':
        d = 'scp41.txt'
    elif data == '2':
        d = 'scp42.txt'
    elif data == '3':
        d = 'scpnrg1.txt'
    elif data == '4':
        d = 'scpnrg2.txt'
    elif data == '5':
        d = 'scpnrg3.txt'
    elif data == '6':
        d = 'scpnrg4.txt'
    elif data == '7':
        d = 'scpnrg5.txt'
    elif data == '8':
        d = 'scpnrh1.txt'
    elif data == '9':
        d = 'scpnrh2.txt'
    elif data == '10':
        d = 'scpnrh3.txt'
    elif data == '11':
        d = 'scpnrh4.txt'
    elif data == '12':
        d = 'scpnrh5.txt'

    archivo = open(d)
    m, n, fo, restricciones = read_data(archivo)

    #ejecución del metodo constructivo
    print('METODO CONSTRUCTIVO')
    Zc = metodo_constructivo(m, n, fo, restricciones)
    print('Valor objetivo con constructivo:', Zc)
    print('')
    #t_final = time.time()


    vo_r = list()
    cot_r = list()
    vo_g1 = list()
    cot_g1 = list()
    vo_g2 = list()
    cot_g2 = list()
    nsol = 10
    for f in range(0,nsol):
        #ejecucion del metodo constructivo con ruido
        print('METODO CONSTRUCTIVO CON RUIDO')
        max_ruido = 1
        vor, cota = constructivo_con_ruido(m, n, fo, restricciones, max_ruido)
        print('')
        #t_final = time.time()
        vo_r.append(vor)
        cot_r.append(cota)

        print('METODO CONSTRUCTIVO CON GRASP POR CARDINALIDAD')
        k = 5
        vog1, cota = grasp1(m, n, fo, restricciones, k)
        print('')
        #t_final = time.time()
        vo_g1.append(vog1)
        cot_g1.append(cota)

        print('METODO CONSTRUCTIVO CON GRASP POR VALORES')
        alpha = 0.5
        vog2, cota = grasp2(m, n, fo, restricciones, alpha)
        #t_final = time.time()
        vo_g2.append(vog2)
        cot_g2.append(cota)

    prom_ruido = sum(vo_r)/nsol
    print('Valor objetivo promedio con ruido:', prom_ruido)
    prom_cota_r = sum(cot_r)/nsol
    print('Valor de la cota promedio con ruido:', prom_cota_r)

    prom_g1 = sum(vo_g1)/nsol
    print('Valor objetivo promedio con grasp1:', prom_g1)
    prom_cota_g1 = sum(cot_g1)/nsol
    print('Valor de la cota promedio con ruido:', prom_cota_g1)

    prom_g2 = sum(vo_g2)/nsol
    print('Valor objetivo promedio con grasp2:', prom_g2)
    prom_cota_g2 = sum(cot_g2)/nsol
    print('Valor de la cota promedio con ruido:', prom_cota_g2)
    #print('Tiempo de computo:', t_final-t_inicial)

Main()