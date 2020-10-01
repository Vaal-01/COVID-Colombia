import matplotlib.pyplot as plot
import sqlite3 as bd
from functions import consultar

#Grafica de barras
def barras_edad(conn,tabla):
    datos = consultar(conn,f"select edad, count(*) as total from {tabla}  where atencion ='Fallecido' group by edad")
    fig, ax = plot.subplots()
    ax.set_ylabel('Fallecidos')
    ax.set_xlabel('Edad')
    ax.set_title('Personas fallecidas por el Covid-19 en Colombia por edad')
    plot.bar(datos['edad'],datos['total'])
    plot.savefig("GraficoBarras_Edad_Fallecidos.png", bbox_inches='tight')

def barras_etnia(conn,tabla):
    datos = consultar(conn,f"select etnia, count(*) as total from {tabla} where etnia ='Negro' or etnia='Indígena' group by etnia")
    fig, ax = plot.subplots()
    ax.set_ylabel('Contagiados')
    ax.set_xlabel('Etnia')
    ax.set_title('Personas contagiadas por el Covid-19 en Colombia segun su etnia')
    plot.bar(datos['etnia'],datos['total'])
    plot.savefig("GraficoBarras_Etnia_Contagios.png", bbox_inches='tight')


#Grafica circular
def cicular_atencion(conn,tabla):
   datos  = consultar(conn,f"select atencion, count(*) as total from {tabla} where atencion != 'CASA' group by atencion")
   fig, ax = plot.subplots(figsize=(10,7))
   plot.title("Estados de personas contagiadas por el Covid-19 en Colombia \n",fontdict={'fontsize':15})
   ax.pie(datos['total'], labels=datos['atencion'], autopct='%1.1f%%',startangle=90)
   ax.axis('equal')
   plot.savefig("GraficaCircular_Estados.png", bbox_inches='tight')

def cicular_Genero(conn,tabla):
   datos  = consultar(conn,f"select sexo, count(*) as total from {tabla} where sexo !='f' and sexo !='m' group by sexo")
   fig, ax = plot.subplots(figsize=(10,7))
   plot.title("Contagios del Covid-19 según el género en Colombia\n",fontdict={'fontsize':15})
   ax.pie(datos['total'], labels=datos['sexo'], autopct='%1.1f%%',startangle=90)
   ax.axis('equal')
   plot.savefig("GraficaCircular_Genero.png", bbox_inches='tight')

#Grafica de dispersion en dos dimensiones
def dosd_contagios(conn,tabla):
    datos  = consultar(conn,f"select edad, count(*) as total from {tabla}  group by edad")
    fig, ax = plot.subplots()
    ax.set_ylabel('Edad')
    ax.set_xlabel('Contagios')
    ax.set_title('Número de personas contagiadas por el Covid-19 según su Edad')
    ax.scatter(datos['total'],datos['edad'])
    plot.savefig("Grafico2d_Edad.png", bbox_inches='tight')

def dosd_ciudad(conn,tabla):
    datos  = consultar(conn,f"select ciudad, count(*) as total from {tabla} where depto=='Vichada' group by ciudad")
    fig, ax = plot.subplots()
    ax.set_ylabel('Ciudades')
    ax.set_xlabel('Contagios')
    ax.set_title('Número de personas contagiadas por el Covid-19 en Vichada por ciudad')
    ax.scatter(datos['total'],datos['ciudad'])
    plot.savefig("Grafico2d_Vichada.png", bbox_inches='tight')