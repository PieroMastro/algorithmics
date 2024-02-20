import pandas as pd

df = pd.read_csv('Python Pro II/M3L3 Limpieza de Datos/googleplaystore.csv')

# Mostrar la aplicación con índice 10472. Vea qué errores se cometieron en los valores.
print("Antes de la corrección:")
print(df.iloc[10472])

# Corrija los errores en los valores
# No parece que sea adecuado mover los valores hacia la derecha para corregir los errores, así que omitimos esta parte.
'''columns = list(df.columns)
index = 10472
for i in range(len(columns) -1, 1, -1):
    df[columns[i]][index] = df[columns[i - 1]][index]'''

# Reemplazar los valores nulos ('NaN') en las columnas 'Category' y 'Genres' con 'LIFESTYLE' y 'Lifestyle' respectivamente.
df.loc[10472, 'Category'] = 'LIFESTYLE'
df.loc[10472, 'Genres'] = 'Lifestyle'

# Mostrar la aplicación para asegurarse de que la limpieza fue exitosa
print("Después de la corrección:")
print(df.iloc[10472])
