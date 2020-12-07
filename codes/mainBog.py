import os

from functions import *
from graphicsBog import *
from regression import *
#from Mapas import MapaBog

#Funcion Principal
def ejecucion():
    #Datos Abiertos del Coronavirus COVID-19 en Bogotá
    url = "https://datosabiertos.bogota.gov.co/dataset/44eacdb7-a535-45ed-be03-16dbbea6f6da/resource/b64ba3c4-9e41-41b8-b3fd-2da21d627558/download/osb_enftransm-covid-19_31_10_2020.csv"
    if os.getcwd():
        database = "covidbg.db"
    tabla = "tablacovidbg"
    conn = conectar(database)
    if verificar(conn, tabla):
        rta = str(input('Hay datos existentes en la base de datos, ¿Quiere actualizarlos? (s/n): '))
        if rta == 's':
            print('Descargando datos, por favor espere')
            actualizarDatosbog(url, conn, tabla)
            print('Se ha actualizado la base de datos de Covid-19 de Bogotá')
    else:
        print('Descargando datos, por favor espere')
        actualizarDatosbog(url, conn, tabla)
        print('Se ha descargado  los datos para la base de datos de Covid-19 de Bogotá')
    print('Comenzando graficación de datos')
    graficarB(conn, tabla)
    #mapasB()
    print('')
    print('Comenzando proyección de datos de COVID en los siguientes meses')
    regresion()
    print('Hasta Luego')
    terminarConexion(conn)


#Generacion graficas
def graficarB(conn, tabla):
    print("La gráficas serán exportadas en formato 'png'. Por favor espere")
    localidad_fallecidos(conn,tabla)
    cicular_GeneroB(conn,tabla)
    dosd_contagiosB(conn,tabla)
    suba(conn, tabla)
    print("Ya se guardaron las gráficas en la carpeta del archivo exitosamente")  

#Generacion mapa   
def mapasB():
    print('Comenzando generación de mapas de calor')
    #MapaBog()
    print('Mapa de Bogotá generado en pagina html')