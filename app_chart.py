import pyodbc
#import plotly.express as px
import plotly.graph_objects as go

conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=d:\Dev\Python\Access\BD_AAE.accdb;')

conn = pyodbc.connect(conn_str)

#criar o cursor
cursor = conn.cursor()

#executar a consulta
dados = cursor.execute("SELECT * FROM [Alunos por nacionalidade]")

rows = cursor.fetchall()

categorias = [row.nacionalidade for row in rows]
values = [row.Contar for row in rows]

#gráfico de barras
#https://plotly.com/python/bar-charts/
#https://chat.openai.com/share/1f2eb289-d59d-450b-a197-6db6baad1811

fig = go.Figure(data=[go.Bar(x=categorias, y=values)])
fig.update_layout(title='Alunos por Nacionalidades',
                  xaxis_title='Nacionalidades',
                  yaxis_title='Contar')

fig.show()

cursor.close()
conn.close()