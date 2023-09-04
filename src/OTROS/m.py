from constructivo import metodo_constructivo
from reading_data import read_data

archivo = open('prueba.txt')
m, n, fo, restricciones = read_data(archivo)

Z0, L0, S0, t0 = metodo_constructivo(m, n, fo, restricciones)
print('Vo:', Z0, '-', 'Seleccionados:', S0)