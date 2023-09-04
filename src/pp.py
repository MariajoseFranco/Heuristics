archivo = open('sol1.txt')
c = list()
for line in archivo:
    a = line.split()
    c.append(a)
for i in c:
    Z0 = i[0]
    L0 = i[1]
    S = i[2:]
    S0 = [int(j) for j in S]
    print(S0)





# import pandas as pd

# b=['scp41.txt','scp42.txt','scpnrg1.txt','scpnrg2.txt','scpnrg3.txt','scpnrg4.txt','scpnrg5.txt','scpnrh1.txt','scpnrh2.txt','scpnrh3.txt','scpnrh4.txt','scpnrh5.txt']
# df = pd.read_excel(r'C:/Users/Asus/Desktop/constructivo_mariajose_franco_orozco.xlsx')
# a = df[:].values.tolist()
# print(a)
# sheet = book.active
# rows = sheet.rows
# for row in rows:
#     a = row[0]
#     print(a)

# df = pd.read_excel (r'C:/Users/Asus/Desktop/constructivo_mariajose_franco_orozco.xlsx',sheet_name=None)
# # print (df['scp41.txt'], df['scp42.txt'])
# df.loc(['526'])
# d = pd.DataFrame(df, columns)
# print(d)

# import xlrd

# loc = ('C:/Users/Asus/Desktop/constructivo_mariajose_franco_orozco.xlsx')
# wb = xlrd.open_workbook(loc)
# sheet = wb.sheet_by_index(0)
# print(sheet.cell_value(0, 0))


# import pandas as pd
# import openpyxl
# from pathlib import Path

# archivo = Path('Escritorio', 'constructivo_mariajose_franco_orozco.xlsx')
# print(archivo)
# wb = openpyxl.load_workbook(archivo)
# hoja = wb.active
# print(hoja['A1'.value])

# archivo = open('C:/Users/Asus/Desktop/constructivo_mariajose_franco_orozco.xlsx')
# e = read_excel(archivo)
# print(e)
# archivo = pd.ExcelFile('C:/Users/Asus/Desktop/constructivo_mariajose_franco_orozco.xlsx')
# dfs = pd.read_excel(archivo, sheet_name='scp41.txt')
# a = dfs.iloc[1]
# print(a)
# Z = dfs[0]
# S = dfs[1,:]
# print(Z, S)
