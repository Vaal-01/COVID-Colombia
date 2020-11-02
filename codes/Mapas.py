import matplotlib.pyplot as plot
import matplotlib.ticker as ticker
import pandas as pd
import sqlite3 as bd
from functions import consultar

#Grafica de barras
def MapaCol(conn,tabla):
    datos = consultar(conn,f"select depto , count(*) as total from {tabla}  GROUP BY depto ORDER BY total DESC")

def MapaBog(conn,tabla):
    datos = consultar(conn,f"select localidad , count(*) as total from {tabla} GROUP BY localidad ORDER BY total DESC")