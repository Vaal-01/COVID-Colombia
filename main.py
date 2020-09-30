from functions import *
#from graphics import *

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
    print('Hasta Luego')
    terminarConexion(conn)


#Manejo de datos
def actualizarDatos(url, conn, tabla):
    data = extraerInformacion(url)
    print('Datos descargados exitosamente.')
    guardarInformacion(conn,data,tabla)
    print('Datos almacenados en la base de datos.')

def verificar(conn, tabla):
    tables = consultar(conn,"SELECT name FROM sqlite_master WHERE type='table'")
    return tables['name'].str.contains(tabla).any()    


#Generacion graficas
def graficar(conn, tabla):
    print('hola')