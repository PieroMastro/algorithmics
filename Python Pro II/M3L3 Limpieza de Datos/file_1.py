import pandas as pd

df = pd.read_csv('Python Pro II/M3L3 Limpieza de Datos/GooglePlayStore_wild.csv')

# Imprimir información sobre todo el DataFrame para ver qué columnas hay que limpiar
print(df.info())
print('=======================================================================')

# ¿Cuántas aplicaciones en el conjunto de datos no tienen ('NaN') clasificación ('Rating')?
print(len(df[pd.isnull(df['Rating'])]))
# Reemplazar el valor nulo ('NaN') de la clasificación ('Rating') para tales aplicaciones con -1.
df['Rating'].fillna(-1, inplace=True)

# Convertir los tamaños ('Size') de aplicación a formato numérico (float). Los tamaños de todas las aplicaciones deben medirse en Megabytes.
def set_size(size):
    if size[-1] == 'M':
        return float(size[:-1])
    elif size[-1] == 'k':
        return float(size[:-1]) / 1024
    return -1

df['Size'] = df['Size'].apply(set_size)

# ¿Cuál es el tamaño máximo 'Size' de las aplicaciones en 'Category' 'TOOLS'?
print(df[df['Category'] == 'TOOLS']['Size'].max())

# Reemplazar el tipo de datos por entero (int) para el número de instalaciones ('Installs').
# En la entrada del número de instalaciones ('Installs'), el signo "+" debe ser ignorado.
# Esto significa que si el número de instalaciones en el conjunto de datos es 1,000,000+, necesita cambiar el valor a 1000000
def set_installs(installs):
    installs = installs.replace('+', '').replace(',', '')
    return int(installs)

df['Installs'] = df['Installs'].apply(set_installs)

# Agrupar los datos por tipo ('Type') y público objetivo ('Content Rating') como prefiera,
# calcular el número promedio de instalaciones ('Installs') para cada grupo Redondear la respuesta a la centésima más cercana.
# En la tabla resultante, encontrar la celda con el mayor valor.
# ¿A qué grupo de edad y tipo de aplicación pertenecen los datos de esa celda?
pivot_table = df.pivot_table(index='Content Rating', columns='Type', values='Installs', aggfunc='mean').round(2)
print(pivot_table)

# ¿Qué aplicación no tiene un 'Type' especificado? ¿Qué tipo debe introducirse allí en función del precio?
print(df[pd.isnull(df['Type'])])
df['Type'].fillna('Free', inplace=True)

# Imprimir información sobre todos los DataFrames para asegurarse de que la limpieza se ha realizado con éxito
print(df.info())
