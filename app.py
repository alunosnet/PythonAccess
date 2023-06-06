import pyodbc

conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=d:\Dev\Python\Access\BD_AAE.accdb;')

conn = pyodbc.connect(conn_str)

#criar o cursor
cursor = conn.cursor()

#executar a consulta
cursor.execute("SELECT * FROM [Alunos por nacionalidade]")

#lista de dados
for row in cursor:
    print(row)

#gráfico de barras
#https://plotly.com/python/bar-charts/

cursor.close()
conn.close()