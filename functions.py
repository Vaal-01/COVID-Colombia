import pandas as pd
import sqlite3 as bd

#Conexion BD
def conectar(database):
    conn = None
    try:
        conn=bd.connect(database)
        print("Se ha conectado a"+database)
        return conn
    except Exception as e:
        print("Lo sentimos no se pudo conectar por"+e)
        exit()

def terminarConexion(conn):
    conn.commit()
    conn.close()

#Manejo informacion
def extraerInformacion(url):
    return pd.read_csv(url)

def guardarInformacion(conn,data,tabla):
    data.to_sql(tabla,conn,schema=None,if_exits='replace',index=False,index_label=None)

def consultar(conn,sentencia):
    return pd.read_sql(sentencia,conn)