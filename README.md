# COVID-Colombia
Script de Python capaz de extraer la información de los datos COVID de la pagina Datos del gobierno 'Datos Abiertos del Coronavirus COVID-19 por ciudad en Colombia', para guardarlos en
una base de datos y representarlos de forma grafica mediante circulos, gráficos de dispersion en dos dimensiones y diagramas de barras.
La extracción de los datos tiene un tiempo de respuesta de varios minutos debido que la base de datos esta compuesta de más de 800.000 registros.  

Para ejecutar el código se utiliza el comando:

\python main.py

Para poder ejecutarlo previamente debe tener instaladas las bibliotecas de: matplotlib.pyplot y pandas. Si no los tiene, escriba los siguientes comandos en su terminal:

\python -m pip install -U pandas

\python -m pip install -U matplotlib
