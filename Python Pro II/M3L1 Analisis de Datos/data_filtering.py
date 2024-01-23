import pandas as pd

df = pd.read_csv ('Python Pro II/M3L1 Analisis de Datos/GoogleApps.csv')

# ¿Cuál es el precio (Price) de la aplicación de pago más barata (Type == 'Paid')?
min_price = df[df['Type'] == 'Paid']['Price'].min()


# Cuál es la mediana (median) del número de instalaciones (Installs)
# de aplicaciones de la categoría "ART_AND_DESIGN" (Category)?
median = df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median()


# ¿Por cuánto el número máximo de reseñas para las aplicaciones gratuitas (Type == 'Free')
# rebasa el número máximo de reseñas para las aplicaciones de pago (Type == 'Paid')?
free = df[df['Type'] == 'Free']['Reviews'].max()
paid = df[df['Type'] == 'Paid']['Reviews'].max()
print(free - paid)


# ¿Cuál es el tamaño mínimo (Size) de una aplicación para adolescentes (Content Rating == 'Teen')?
min_teen_size = df[df['Content Rating'] == 'Teen']['Size'].min()


# *¿Cuál es la categoría (Category) de una aplicación con el mayor número de reseñas (Reviews)?
category_max_reviews= df[df['Reviews'] == df['Reviews'].max()]['Category']


# ¿Cuál es la valoración (Rating) media (mean) de las aplicaciones con un precio (Price) superior a $ 20 y 
# con el número de instalaciones (Installs) más de 10.000?
print(df[(df['Price'] > 20) & (df['Installs'] > 10000)]['Rating'].mean())
