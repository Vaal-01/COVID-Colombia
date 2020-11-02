import os
from functions import *
from graphics import *
#from Mapas import MapaCol
from mainBog import ejecucion

#Funcion Principal
def main(url, database, tabla):
    print('DATOS ESPECÍFICOS DE COLOMBIA :D')
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
    #mapas()
    terminarConexion(conn)
    print('DATOS ESPECÍFICOS DE BOGOTÁ :D') 
    ejecucion()

#Generacion graficas
def graficar(conn, tabla):
    print("La gráficas serán exportadas en formato 'png'. Por favor espere")
    barras_edad(conn,tabla)
    barras_rec(conn,tabla)
    cicular_atencion(conn,tabla)
    cicular_Genero(conn,tabla)
    edades(conn,tabla)
    contagios(conn,tabla)
    ciudad(conn,tabla)
    fechas(conn,tabla)
    fechasmuerte(conn,tabla)
    print("Ya se guardaron las gráficas en la carpeta del archivo exitosamente")  

#Generacion mapa   
def mapas():
    print('Comenzando generación de mapas de calor')
   # MapaCol()
    print('Mapa de Colombia generado en pagina html')

#Funcionamiento
if __name__ == '__main__':
    #Datos Abiertos del Coronavirus COVID-19 por ciudad en Colombia
    url = "https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD&amp;bom=true&amp;format=true"
    if os.getcwd():
        database = "covid19.db"
    tabla = "tablacovid"
    main(url, database, tabla)