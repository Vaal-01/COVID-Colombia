import matplotlib.pyplot as plot
import matplotlib.ticker as ticker
import pandas as pd
import sqlite3 as bd
from functions import consultar

#Grafica de barras
def localidad_fallecidos(conn,tabla):
    datos = consultar(conn,f"SELECT localidad, count(*) as cantidad FROM {tabla} WHERE localidad!='Sin dato' and estado='Fallecido' GROUP BY localidad ORDER BY cantidad")
    datos.plot(x='localidad', y='cantidad', kind='barh', xlabel='Localidad', ylabel='Fallecidos',color='Orange')
    plot.title('Fallecidos por localidad')
    plot.savefig("plotsBogota/Graficolocalidad.png", bbox_inches='tight')

#Grafica circular
def cicular_GeneroB(conn,tabla):
   datos  = consultar(conn,f"select sexo, count(*) as total from {tabla} where sexo !='f' and sexo !='m' and localidad='Kennedy'group by sexo")
   fig, ax = plot.subplots(figsize=(10,7))
   plot.title("Contagios del Covid-19 según el género en la locaildad de Kennedy\n",fontdict={'fontsize':15})
   ax.pie(datos['total'], labels=datos['sexo'], autopct='%1.1f%%',startangle=90)
   ax.axis('equal')
   plot.savefig("plotsBogota/GraficaCircular_GeneroK.png", bbox_inches='tight')
   
#Grafica de dispersion 
def dosd_contagiosB(conn,tabla):
    datos  = consultar(conn,f"select localidad, count(*) as total from {tabla} where sexo='F' group by localidad")
    fig, ax = plot.subplots()
    ax.set_ylabel('Localidades')
    ax.set_xlabel('hombres Contagiados')
    ax.set_title('Número de hombres contagiados por el Covid-19 en Bogotá por localidad')
    ax.scatter(datos['total'],datos['localidad'])
    plot.savefig("plotsBogota/Grafico_Locali.png", bbox_inches='tight')

#Grafica de dos dimensiones
def suba(conn,tabla):
    datos = consultar(conn,f"SELECT fecha_diag, count(*) as cantidad FROM {tabla} WHERE fecha_diag not null and localidad='Suba' GROUP BY fecha_diag ORDER BY fecha_diag" )
    datos['fecha_diag'] = pd.to_datetime(datos['fecha_diag'])
    datos['fecha_diag'] = datos['fecha_diag'].dt.strftime("%m-%d")
    datos.plot(x='fecha_diag', y='cantidad', xlabel='Tiempo', ylabel='Contagios',color='green')
    plot.title('Contagiados contra el tiempo de la localidad Suba en Bogotá')
    plot.savefig("plotsBogota/Graficocontagios.png")