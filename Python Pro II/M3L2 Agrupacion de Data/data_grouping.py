import pandas as pd

df = pd.read_csv ('Python Pro II/M3L1 Analisis de Datos/GoogleApps.csv')
print(df.info())

print('--------------------------------------------')

# ¿Cuántas veces el número de aplicaciones para el público "todos los usuarios"
# supera el número de aplicaciones para los usuarios "10+"?

temp = df['Content Rating'].value_counts()
print(temp)

print('--------------------------------------------')

#print(temps['Everyone'])
everyone = temp['Everyone']
everyone_10 = temp['Everyone 10+']
print(everyone / everyone_10)

print('--------------------------------------------')

#¿Cuál es el tamaño promedio de aplicación para cada público objetivo?

print(df.groupby(by = 'Content Rating')['Size'].mean())

print('--------------------------------------------')


# ¿Cuáles son los tamaños mínimos y máximos de las apps pagas y gratuitas para cada audiencia objetivo?

print(df.groupby(by = 'Content Rating')['Size'].agg(['min', 'max']))

print('--------------------------------------------')

# Comparando data para multiples objetivos:

data = df.groupby(by = ['Type', 'Content Rating'])['Size'].agg(['min', 'max'])
print(data)
print(data['min']['Free']['Teen'])
print(data.reset_index())

print('--------------------------------------------')

print(df.pivot_table
    (
        columns = 'Type', 
        index = 'Content Rating', 
        values = 'Size', 
        aggfunc = ['min', 'max']
    ))



