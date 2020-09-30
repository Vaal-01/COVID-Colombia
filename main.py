import os

from functions import *
from graphics import *

#Funcion Principal
def main(url, database, tabla):
    conn = conectar(database)
    if verificar(conn, tabla):
        rta = str(input('Hay datos existentes en la base de datos, ¿Quiere actualizarlos? (s/n): '))
        if rta == 's':
            actualizarDatos(url, conn, tabla)
            print('Se ha actualizado la base de datos de Covid-19')
    else:
        actualizarDatos(url, conn, tabla)
        print('Se ha descargado  los datos para la base de datos de Covid-19')

    print('Comenzando graficacion de datos')
    graficar(conn, tabla)
    print('Hasta Luego :D')
    terminarConexion(conn)


#Manejo de datos
def actualizarDatos(url, conn, tabla):
    data = extraerInformacion(url)
    print('Datos descargados exitosamente.')
    data = quitarEspacios(data)
    guardarInformacion(conn,data,tabla)
    print('Datos almacenados en la base de datos.')

def verificar(conn, tabla):
    tables = consultar(conn,"SELECT name FROM sqlite_master WHERE type='table'")
    return tables['name'].str.contains(tabla).any()    

def quitarEspacios(data):
    return data.rename(columns={
        'ID de caso': 'id_caso','Fecha de notificación':'fecha_notificacion','Código DIVIPOLA': 'cod_divipola','Ciudad de ubicación': 'ciudad',
        'Departamento o Distrito ': 'depto','atención': 'atencion','Edad': 'edad','Sexo': 'sexo', 'Estado': 'estado', 'Tipo':'tipo'
        'País de procedencia': 'pais_procedencia', 'FIS': 'FIS','Fecha de muerte': 'fecha_muerte','Fecha diagnostico': 'fecha_diagnostico',
        'Fecha recuperado': 'fecha_recuperado','fecha reporte web': 'fecha_web', 'Tipo recuperación': 'tipo_recuperacion',
        'Codigo departamento': 'cod_depto','Codigo pais': 'cod_pais','Pertenencia etnica': 'etnia','Nombre grupo etnico': 'nom_etnia'
    })

#Generacion graficas
def graficar(conn, tabla):
    print("Gráficos de barras")  
    barras_edad(conn,tabla)
    print("Gráficas circulares")  
    cicular_estado(conn,tabla)
    print("Gráficas de dos dimensiones")  

#Funcionamiento
def ejecutar():
    #Datos Abiertos del Coronavirus COVID-19 por ciudad en Colombia
    url = "https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD"
    in os.getcwd():
        database = "datos/covid19.db"
    tabla = "tablacovid"

if __name__ == '__main__':
    ejecutar()
    main(url, database, tabla)