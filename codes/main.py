import os

from functions import *
from graphics import *

#Funcion Principal
def main(url, database, tabla):
    conn = conectar(database)
    if verificar(conn, tabla):
        rta = str(input('Hay datos existentes en la base de datos, ¿Quiere actualizarlos? (s/n): '))
        if rta == 's':
            print('Descargando datos, por favor espere')
            actualizarDatos(url, conn, tabla)
            print('Se ha actualizado la base de datos de Covid-19')
    else:
        print('Descargando datos, por favor espere')
        actualizarDatos(url, conn, tabla)
        print('Se ha descargado  los datos para la base de datos de Covid-19')

    print('Comenzando graficación de datos')
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
    tables = consultar(conn,f"SELECT name FROM sqlite_master WHERE type='table'")
    return tables['name'].str.contains(tabla).any()    

def quitarEspacios(data):
    return data.rename(columns={
        'fecha reporte web':'fecha_reporte','ID de caso': 'id_caso','Fecha de notificación':'fecha_notificacion','Código DIVIPOLA departamento': 'cod_divipola', 
        'Nombre departamento': 'depto','Código DIVIPOLA municipio': 'cod_divipolamun','Nombre municipio': 'municipio','Edad': 'edad','Unidad de medida de edad': 'unidad_edad',
        'Sexo': 'sexo', 'Tipo de contagio':'tipo','Ubicación del caso': 'ubicacion_caso','Estado': 'estado','Código ISO del país':'iso','Nombre del país':'pais_procedencia',
        'Recuperado': 'recuperado','Fecha de inicio de síntomas': 'fecha_sintomas','Fecha de muerte': 'fecha_muerte','Fecha de diagnóstico':'fecha_diagnostico',
        'Fecha de recuperación': 'fecha_recuperado', 'Tipo de recuperación': 'tipo_recuperacion','Pertenencia étnica': 'etnia',
        'Nombre del grupo étnico': 'nombre_etnia'
    })

#Generacion graficas
def graficar(conn, tabla):
    print("La gráficas serán exportadas en formato 'png'. Por favor espere")
    barras_edad(conn,tabla)
    barras_rec(conn,tabla)
    cicular_atencion(conn,tabla)
    cicular_Genero(conn,tabla)
    dosd_contagios(conn,tabla)
    dosd_ciudad(conn,tabla)
    fechas(conn,tabla)
    fechasmuerte(conn,tabla)
    
    print("Ya se guardaron las gráficas en la carpeta del archivo exitosamente")  

#Funcionamiento
if __name__ == '__main__':
    #Datos Abiertos del Coronavirus COVID-19 por ciudad en Colombia
    url = "https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD&amp;bom=true&amp;format=true"
    if os.getcwd():
        database = "covid19.db"
    tabla = "tablacovid"
    main(url, database, tabla)