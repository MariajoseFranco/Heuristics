# Algoritmo para leer los datos y separar las restricciones y la funcion objetivo


def read_data(f):
    #de los datos hacer una lista de listas en la que cada posicion de la lista es un renglon del documento txt y cada lista dentro de esa
    #posicion es una lista de str que contiene los datos del respectivo renglon
    c = list()
    for line in f:
        a = line.split()
        c.append(a)

    #crear una lista con todos los datos en tipo entero
    datos_en_lista = list()
    for sublist in c:
        for item in sublist:
            datos_en_lista.append(int(item))

    #Valores m y n
    m = datos_en_lista[0]
    n = datos_en_lista[1]

    #Costos de la funcion objetivo (FO)
    fo = list()
    for i in range(2,n+2):
        fo.append(datos_en_lista[i])

    #organizar las restricciones
    datos_en_lista_restricciones = datos_en_lista[:]
    for i in range(0,n+2):
        datos_en_lista_restricciones.pop(0)

    restricciones = list()
    tamaño = len(datos_en_lista_restricciones)
    for j in range(0,tamaño):
        res = list()
        indicador = datos_en_lista_restricciones[0]
        datos_en_lista_restricciones.pop(0)
        for k in range(0,indicador):
            res.append(datos_en_lista_restricciones[0])
            datos_en_lista_restricciones.pop(0)
        restricciones.append(res)
        tamaño = len(datos_en_lista_restricciones)
        if tamaño == 0:
            break
    return m, n, fo, restricciones