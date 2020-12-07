import matplotlib.pyplot as plot
import matplotlib.ticker as ticker
import pandas as pd
import sqlite3 as bd
from functions import consultar

#Grafica de barras
def barras_edad(conn,tabla):
    datos = consultar(conn,f"select edad, count(*) as total from {tabla}  where recuperado ='Fallecido' group by edad")
    fig, ax = plot.subplots()
    ax.set_ylabel('Fallecidos')
    ax.set_xlabel('Edad')
    ax.set_title('Personas fallecidas por el Covid-19 en Colombia por edad')
    plot.bar(datos['edad'],datos['total'])
    plot.savefig("plotsColombia/GraficoBarras_Edad_Fallecidos.png", bbox_inches='tight')

def barras_rec(conn,tabla):
    datos = consultar(conn,f"select tipo_recuperacion, count(*) as total from {tabla} where tipo_recuperacion ='PCR' or tipo_recuperacion='Tiempo' group by tipo_recuperacion")
    fig, ax = plot.subplots()
    ax.set_ylabel('Recuperados')
    ax.set_xlabel('Tipo de Recuperación')
    ax.set_title('Personas recuperadas del Covid-19 en Colombia segun su tipo de recuperacion')
    plot.bar(datos['tipo_recuperacion'],datos['total'])
    plot.savefig("plotsColombia/GraficoBarras_recuperacion.png", bbox_inches='tight')

#Grafica circular
def cicular_atencion(conn,tabla):
   datos  = consultar(conn,f"select ubicacion_caso, count(*) as total from {tabla} where ubicacion_caso != 'CASA' and ubicacion_caso != 'Hospital UCI' group by ubicacion_caso")
   fig, ax = plot.subplots(figsize=(10,7))
   plot.title("Estados de personas contagiadas por el Covid-19 en Colombia \n",fontdict={'fontsize':15})
   ax.pie(datos['total'], labels=datos['ubicacion_caso'], autopct='%1.1f%%',startangle=90, normalize=True)
   ax.axis('equal')
   plot.savefig("plotsColombia/GraficaCircular_Estados.png", bbox_inches='tight')

def cicular_Genero(conn,tabla):
   datos  = consultar(conn,f"select sexo, count(*) as total from {tabla} where sexo !='f' and sexo !='m' group by sexo")
   fig, ax = plot.subplots(figsize=(10,7))
   plot.title("Contagios del Covid-19 según el género en Colombia\n",fontdict={'fontsize':15})
   ax.pie(datos['total'], labels=datos['sexo'], autopct='%1.1f%%',startangle=90, normalize=True)
   ax.axis('equal')
   plot.savefig("plotsColombia/GraficaCircular_Genero.png", bbox_inches='tight')

#Grafica de dispersion 
def edades(conn,tabla):
    datos  = consultar(conn,f"select edad, count(*) as total from {tabla}  group by edad")
    fig, ax = plot.subplots()
    ax.set_ylabel('Edad')
    ax.set_xlabel('Contagios')
    ax.set_title('Número de personas contagiadas por el Covid-19 según su Edad')
    ax.scatter(datos['total'],datos['edad'])
    plot.savefig("plotsColombia/Grafico_Edad.png", bbox_inches='tight')

def contagios(conn,tabla):
    datos  = consultar(conn,f"select municipio, count(*) as total from {tabla} where depto=='RISARALDA' and  recuperado ='Fallecido' group by municipio")
    fig, ax = plot.subplots()
    ax.set_ylabel('Ciudades')
    ax.set_xlabel('Fallecidos')
    ax.set_title('Número de personas fallecidas por el Covid-19 en Risaralda por ciudad ')
    ax.scatter(datos['total'],datos['municipio'])
    plot.savefig("plotsColombia/Grafico_Depto.png", bbox_inches='tight')

def ciudad(conn,tabla):
    datos  = consultar(conn,f"select municipio, count(*) as total from {tabla} where depto=='VICHADA' group by municipio")
    fig, ax = plot.subplots()
    ax.set_ylabel('Ciudades')
    ax.set_xlabel('Contagios')
    ax.set_title('Número de personas contagiadas por el Covid-19 en Vichada por ciudad')
    ax.scatter(datos['total'],datos['municipio'])
    plot.savefig("plotsColombia/Grafico2d_Vichada.png", bbox_inches='tight')

#Grafica de dos dimensiones
def fechas(conn, tabla):
    datos = consultar(conn,f"select fecha_notificacion, count(*) as cantidad FROM {tabla} group by fecha_notificacion ORDER BY fecha_notificacion")
    datos['fecha_notificacion'] = pd.to_datetime(datos['fecha_notificacion'])
    datos['fecha_notificacion'] = datos['fecha_notificacion'].dt.strftime("%m-%d")
    xinf = datos['fecha_notificacion']
    yinf = datos['cantidad']
    fig, ax = plot.subplots()
    plot.title('Curva de contagiados en el tiempo')
    ax.plot(xinf, yinf,'green')
    plot.legend(['Contagiados'])
    loc = ticker.MultipleLocator(base=20)
    ax.xaxis.set_major_locator(loc)
    plot.savefig("plotsColombia/Graficocontagios.png", bbox_inches='tight')


def fechasmuerte(conn, tabla):
    datos = consultar(conn,f"select fecha_notificacion, count(*) as cantidad FROM {tabla} group by fecha_notificacion ORDER BY fecha_notificacion")
    datos['fecha_notificacion'] = pd.to_datetime(datos['fecha_notificacion'])
    datos['fecha_notificacion'] = datos['fecha_notificacion'].dt.strftime("%m-%d")
    xinf = datos['fecha_notificacion']
    yinf = datos['cantidad']
    datosm = consultar(conn,f"select fecha_muerte, count(*) as cantidad FROM {tabla} WHERE fecha_muerte IS NOT NULL GROUP BY fecha_muerte ORDER BY fecha_muerte")
    datosm['fecha_muerte'] = pd.to_datetime(datosm['fecha_muerte'])
    datosm['fecha_muerte'] = datosm['fecha_muerte'].dt.strftime("%m-%d")
    xmuer = datosm['fecha_muerte']
    ymuer = datosm['cantidad']
    fig, ax = plot.subplots()
    plot.title('Curva de comparación de muertos y recuperados en el tiempo')
    ax.plot(xinf, yinf)
    ax.plot(xmuer, ymuer,'red')
    plot.legend(['Contagiados','Muertos'])
    loc = ticker.MultipleLocator(base=20)
    ax.xaxis.set_major_locator(loc)
    plot.savefig("plotsColombia/Graficomuerte.png", bbox_inches='tight')