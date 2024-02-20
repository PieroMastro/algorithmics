import pandas as pd

df = pd.read_csv('Python Pro II/M3L1 Analisis de Datos/GoogleApps.csv')
print(df.info())
print('--------------------------------------------')

#1 ¿Cuántas aplicaciones hay en la 'Category' 'BUSINESS'?
print(df['Category'].value_counts())


#2 ¿Cuál es la relación de aplicaciones para adolescentes ('Teen') y las destinadas para niños mayores de 10 años ('Everyone 10+')?
#Redondee la respuesta a la centésima más cercana.
temp = df['Content Rating'].value_counts()
print('Ratio:', round(temp['Teen'] / temp['Everyone 10+'], 2))


#3.1 ¿Cuál es el 'Rating' promedio de aplicaciones 'Paid'?
#Redondee la respuesta a la centésima más cercana.
temp = df.groupby(by = 'Type')['Rating'].mean()
print(temp['Paid'])


#3.2 ¿Cuánto más bajo es el 'Rating' promedio de aplicaciones 'Free' que el promedio de valoración de las aplicaciones 'Paid'?
#Redondee la respuesta a la centésima más cercana.
print(round(temp['Paid'] - temp['Free'], 2))


#4 ¿Cuál es el 'Size' (tamaño) mínimo y máximo en la 'Category' 'COMICS'?
#Redondee la respuesta a la centésima más cercana.
print(df.groupby(by = 'Category')['Size'].agg(['min', 'max']))


#Bonificación 1. ¿Cuántas aplicaciones tienen un 'Rating' de más de 4.5 en la 'Category' 'FINANCE'?
temp = df[df['Rating'] > 4.5]['Category'].value_counts()
print(temp['FINANCE'])


#Bonificación 2. ¿Cuál es la relación de juegos 'Free' y 'Paid' con un 'Rating' superior a 4.9?
temp = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(temp['Free'] / temp['Paid'])
