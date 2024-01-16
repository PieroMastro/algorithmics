import pandas as pd

# Cargar el marco de datos
df = pd.read_csv ('Python Pro II/M3L1 Analisis de Datos/GoogleApps.csv')

# ¿Cuál es el nombre de la primera aplicación en el conjunto de datos?
print(df.head())

# ¿A qué categoría pertenece la última aplicación del conjunto de datos?
print(df.tail())

# ¿Cuántas columnas hay en el conjunto de datos?
# ¿Qué tipo de datos se almacenan en cada una de las columnas?
print(df.info())


# Especifique la media aritmética y la mediana del tamaño de la aplicación (Tamaño)
# ¿Cuánto cuesta la aplicación más cara?
# * Especifique la media aritmética y la mediana del número de instalaciones de aplicaciones (Instalaciones)
print(df.describe())