import matplotlib.pyplot as plot

import numpy as np
import requests
import pandas as pd
import numpy as np
from numpy.linalg import inv
import os

#Proyecciones de contagio a dos meses
#Datos en csv 

def regresion():  
    print('Por favor espere .. ')
    url="https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD&bom=true&format=true"
    response = requests.get(url)
    with open(os.path.join("DatosColombia.csv"), "wb") as f:
         f.write(response.content)
    data =pd.read_csv('DatosColombia.csv',low_memory=False)
    data.columns=['Fecha', 'ID', 'Fecha2', 'Código DIVIPOLA', 'depto', 'Código DIVIPOLA2', 'Ciudad','Edad','Unnidad', 'Sexo', 'Tipo', 'Ubicacion','Atencion', 'Código ISO del país','Nombre del país','Recuperado','Fecha de inicio de síntomas','Fecha de muerte','Fecha de diagnóstico','Fecha de recuperación','Tipo de recuperación','Pertenencia étnica','Nombre del grupo étnico']
    data['Fecha']= pd.to_datetime(data['Fecha'])
    #Grafica inicial 
    info1=data.Fecha[data.Fecha.dt.month != 12.0].dt.month.value_counts().index.unique()
    info2=data.Fecha[data.Fecha.dt.month != 12.0].dt.month.value_counts()
    fig, ax = plot.subplots()
    ax.scatter(info1,info2)
    ax.set_ylabel('Número de Casos')
    ax.set_xlabel('Meses')
    ax.set_title('Gráfica de la información de casos en Colombia')
    plot.savefig("proyeccion_regression/Graficainicial.png", bbox_inches='tight')

    #Regresion lineal
    X=np.array([np.ones(len(info1)),info1]).T
    a= inv(X.T @ X ) @X.T @ info2
    x_predict=np.linspace(3,11,num=100) 
    subs_predict=a[0]+a[1]*x_predict 
    fig, ax = plot.subplots()
    ax.scatter(info1,info2)
    ax.set_ylabel('Número de Casos')
    ax.set_xlabel('Meses')
    ax.set_title('Regresión Lineal de los Datos de Covid en Colombia')
    plot.plot(x_predict, subs_predict,'c')
    plot.savefig("proyeccion_regression/Grafica_regresion_lineal.png", bbox_inches='tight')

    #Proyecciones Dos meses
    #Pendiente a[1]
    #x = 12 o 13 para la proyeccion del mes 
    
    archivo = open("proyeccion_regression/proyeccion.txt", "w")

    #Mes 1 - Diciembre
    y= a[1]*(12)+a[0] 
    y1=f"{y:.1f}"
    archivo.write("Proyección Mes 1: Diciembre 2020\n") 
    archivo.write("Para finales de este mes se estima que existirán "+(y1)+" casos en Colombia.\n") 
    archivo.write("\n") 

    #Mes 2 - Enero
    y= a[1]*(13)+a[0] 
    y1=f"{y:.1f}"
    archivo.write("Proyección Mes 2: Enero 2021\n") 
    archivo.write("Para finales de este mes se estima que existirán "+(y1)+" casos en Colombia.\n") 
    
    archivo.close()
    print('Las gráficas respectivas a la regresión y el archivo txt con los resultados de las proyecciones se encuentran en la carpeta "proyeccion_regression"')
    print('')
   
    