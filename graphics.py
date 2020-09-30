import matplotlib.pyplot as plot
import sqlite3 as bd

#Grafica de barras
def barras_edad(conn,tabla):
    cursor = conn.cursor()
    datos = cursor.execute("select edad, count(*) as total from {tabla}  where atencion ='Fallecido' group by edad")
    plot.figure()
    plot.title('Personas fallecidas por edad')
    plot.barh(datos['edad'],datos['total'])
    plot.show()

#Grafica circular
def cicular_estado(conn,tabla):
    cursor = conn.cursor()
    datos  = cursor.execute("select atencion, count(*) total from {tabla} group by atencion")
    plot.figure()
    plot.title('Número de personas segun el estado')
    plot.pie(datos['total'],labels=['Recuperado','Fallecido'],shadow=True)
    plot.show()

#Grafica de dos dimensiones
def dosd_contagios(conn,tabla):
    cursor = conn.cursor()
    datos  = cursor.execute("select sexo, count(*) as total from {tabla} where depto='Antioquia' group by sexo")
    f = plot.figure()
    ax = f.add_subplots()
    plot.title('Personas según genero contagiados en Antioquia')
    plot.xlabel('Género')
    plot.ylabel('Contagiados')
    ax.scatter(datos['sexo'],datos['total'])
    plot.show()