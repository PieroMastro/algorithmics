import pandas as pd

# Cargar el marco de datos
df = pd.read_csv ('Python Pro II/M3L1 Analisis de Datos/GoogleApps.csv')

# ¿Cuál es el nombre de la primera aplicación en el conjunto de datos?
'Photo Editor & Candy Camera & Grid & ScrapBook'
print(df.head())

# ¿A qué categoría pertenece la última aplicación del conjunto de datos?
'LIFESTYLE'
print(df.tail())

# ¿Cuántas columnas hay en el conjunto de datos?
'12'
# ¿Qué tipo de datos se almacenan en cada una de las columnas?
'object, int64, float64'
print(df.info())

# Especifique la media aritmética y la mediana del tamaño de la aplicación (Tamaño)
'22.769578, 14'
# ¿Cuánto cuesta la aplicación más cara?
'400'
# * Especifique la media aritmética y la mediana del número de instalaciones de aplicaciones (Instalaciones)
'8662313, 10000'
print(df.describe())