import pandas as pd
import sqlite3 as bd

#Conexion BD
def conectar(database):
    conn = None
    try:
        conn=bd.connect(database)
        print("Se ha conectado a "+database)
        return conn
    except Exception as e:
        print(e)
        exit()

def terminarConexion(conn):
    conn.commit()
    conn.close()

#Manejo informacion
def extraerInformacion(url):
    return pd.read_csv(url,low_memory=False)

def extraerInformacionB(url):
    return pd.read_csv(url, error_bad_lines=False)

def guardarInformacion(conn,data,tabla):
    data.to_sql(tabla,conn,schema=None,if_exists='replace',index=False,index_label=None)

def consultar(conn,sentencia):
    return pd.read_sql(sentencia,conn)

def actualizarDatos(url, conn, tabla):
    data = extraerInformacion(url)
    print('Datos descargados exitosamente.')
    data = quitarEspacios(data)
    guardarInformacion(conn,data,tabla)
    print('Datos almacenados en la base de datos.')

def guardarBog(url):
    return pd.read_csv(url, sep=";", engine='python', encoding = "ISO-8859-1", dayfirst=True, parse_dates=['FECHA_DIAGNOSTICO', 'FECHA_INICIO_SINTOMAS'])

def actualizarDatosbog(url,conn,tabla):
    data = guardarBog(url)
    print('Datos descargados exitosamente.')
    data = rename(data)
    guardarInformacion(conn, data,tabla)
    print('Datos almacenados en la base de datos.')

def verificar(conn, tabla):
    tables = consultar(conn,f"SELECT name FROM sqlite_master WHERE type='table'")
    return tables['name'].str.contains(tabla).any()   


#Manejo de datos

def quitarEspacios(data):
    return data.rename(columns={
        'fecha reporte web':'fecha_reporte','ID de caso': 'id_caso','Fecha de notificación':'fecha_notificacion','Código DIVIPOLA departamento': 'cod_divipola', 
        'Nombre departamento': 'depto','Código DIVIPOLA municipio': 'cod_divipolamun','Nombre municipio': 'municipio','Edad': 'edad','Unidad de medida de edad': 'unidad_edad',
        'Sexo': 'sexo', 'Tipo de contagio':'tipo','Ubicación del caso': 'ubicacion_caso','Estado': 'estado','Código ISO del país':'iso','Nombre del país':'pais_procedencia',
        'Recuperado': 'recuperado','Fecha de inicio de síntomas': 'fecha_sintomas','Fecha de muerte': 'fecha_muerte','Fecha de diagnóstico':'fecha_diagnostico',
        'Fecha de recuperación': 'fecha_recuperado', 'Tipo de recuperación': 'tipo_recuperacion','Pertenencia étnica': 'etnia',
        'Nombre del grupo étnico': 'nombre_etnia'
    })

def rename(data):
    return data.rename(columns={
        'FECHA_INICIO_SINTOMAS':'fecha_sintomas','FECHA_DIAGNOSTICO': 'fecha_diag','CIUDAD':'ciudad','LOCALIDAD_ASIS': 'localidad', 
        'EDAD': 'edad','UNI_MED': 'unidad_edad','SEXO': 'sexo', 'FUENTE_O_TIPO_CONTAGIO':'tipo','UBICACION': 'ubicacion','ESTADO': 'estado'
         })