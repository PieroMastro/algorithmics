import pandas as pd

df = pd.read_csv('Python Pro II/M3L3 Limpieza de Datos/GooglePlayStore_wild.csv')

# Limpieza de datos de la primera tarea
df['Rating'].fillna(-1, inplace = True)


def set_size(size):
    if size[-1] == 'M':
        return float(size[:-1])
    elif size[-1] == 'k':
        return float(size[:-1]) / 1024
    return -1
df['Size'] = df['Size'].apply(set_size)


def set_installs(installs):
    if installs == '0':
        return 0
    return int(installs[:-1].replace(',', ''))
df['Installs'] = df['Installs'].apply(set_installs)


df['Type'].fillna('Free', inplace = True)


# Reemplazar el tipo de datos por un número fraccionario (float) para los precios de la aplicación ('Price')
def make_price(price):
    if price[0] == '$':
        return float(price[1:])
    return 0           
df['Price'] = df['Price'].apply(make_price)


# Calcular cuántos dólares han ganado los desarrolladores con cada aplicación de pago
df['Profit'] = df['Installs'] * df['Price']


# ¿Cuáles son las mayores ganancias ('Profit') entre las aplicaciones de pago (Type == 'Paid')?
print(df[df['Type'] == 'Paid']['Profit'].max())


# Crear una nueva columna que almacenará el número de géneros. Llamarla 'Number of genres'
def split_genres(genres):
    return genres.split(';')


df['Genres'] = df['Genres'].apply(split_genres)
df['Number of genres'] = df['Genres'].apply(len)


# ¿Cuál es el máximo 'Number of genres' almacenado en el conjunto de datos?
print(df['Number of genres'].max())


# Tarea adicional
# Crear una nueva columna que almacene la estación en la que la aplicación fue actualizada por última vez 'Last Updated'. Llamarla 'Season'
def set_season(date):
    month = date.split()[0]
    seasons = {'Winter': ['December', 'January', 'February'],
                'Spring': ['March', 'April', 'May'],
                'Summer': ['June', 'July', 'August'],
                'Autumn': ['September', 'October', 'November']}
    for season in seasons:
        if month in seasons[season]:
            return season
    return 'Season not identified'


df['Season'] = df['Last Updated'].apply(set_season)


# Mostrar las estaciones y cuántas hay en el conjunto de datos
print(df['Season'].value_counts())
