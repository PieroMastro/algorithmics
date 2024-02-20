import pandas as pd

df = pd.read_csv ('Python Pro II/M3L1 Analisis de Datos/GoogleApps.csv')
print(df.info())

install_mayor_49 = df[df['Rating']>4.9]['Installs'].mean()
print(install_mayor_49) # Filtramos las apps con rating > 4.9
print('Número promedio de descargas (Installs) de apps con calificación (Rating) exceda el valor de 4.9:')
print(df[df['Rating']>4.9]['Installs'].mean()) # Filtramos de nuevo por el parametro 'installs' y aplicamos la funcion mean() para determinar el promedio

#  Número promedio de descargas (Installs) de apps gratuitas (Type == 'Free')
#  con una calificación (Rating) que supere 4.9
print(df[(df['Type'] =='Free') & (df['Rating'] > 4.9)]['Installs'].mean())

# ¿Cuál es el precio (Price) de la aplicación de pago más barata (Type == 'Paid')?
print(df[df['Type'] == 'Paid']['Price'].min())

# Cuál es la mediana (median) del número de instalaciones (Installs)
# de aplicaciones de la categoría "ART_AND_DESIGN" (Category)?
print(df[df['Category'] == "ART_AND_DESIGN"]['Installs'].median())

# ¿Por cuánto el número máximo de reseñas para las aplicaciones gratuitas (Type == 'Free')
# rebasa el número máximo de reseñas para las aplicaciones de pago (Type == 'Paid')?
free = df[df['Type'] == 'Free']['Reviews'].max()
paid = df[df['Type'] == 'Paid']['Reviews'].max()
print(free - paid)

# ¿Cuál es el tamaño mínimo (Size) de una aplicación para adolescentes (Content Rating == 'Teen')?
min_size_teen = df[df['Content Rating'] == 'Teen']['Size'].min()
print(round(min_size_teen, 3))

# *¿Cuál es la categoría (Category) de una aplicación con el mayor número de reseñas (Reviews)?
max_reviews = df[df['Reviews'] == df['Reviews'].max()]['Category']
print(max_reviews)

# ¿Cuál es la valoración (Rating) media (mean) de las aplicaciones con un precio (Price) superior a $ 20 y 
# con el número de instalaciones (Installs) más de 10.000?

question_5 = df[(df['Price'] > 20) & (df['Installs']>10000)]['Rating'].mean()
print(question_5)