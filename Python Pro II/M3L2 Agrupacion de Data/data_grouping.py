import pandas as pd

df = pd.read_csv('Python Pro II/M3L1 Analisis de Datos/GoogleApps.csv')
print(df.info())
print('--------------------------------------------')

# ¿Cuántas veces el número de aplicaciones para el público "todos los usuarios"
# supera el número de aplicaciones para los usuarios "10+"?
content = df['Content Rating'].value_counts()
print(content)
print('--------------------------------------------')
everyone = content['Everyone']
everyone_10 = content['Everyone 10+']
print(everyone/everyone_10)

print('--------------------------------------------')

#¿Cuál es el tamaño promedio de aplicación para cada público objetivo?
average_all = df.groupby(by = 'Content Rating')['Size'].agg(['min', 'max'])
print(average_all)
print('--------------------------------------------')


# ¿Cuáles son los tamaños mínimos y máximos de las apps pagas y gratuitas para cada audiencia objetivo?


print('--------------------------------------------')

# Comparando data para multiples objetivos:


print('--------------------------------------------')


