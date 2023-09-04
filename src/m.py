from r import read_file

datos = [
        'scp41.txt','scp42.txt']

for i in datos:
    m, n, fo, restricciones = read_file(i)
    print('')
    print('\t', m,'\t',n,'\t',fo,'\t',restricciones)
    print('')