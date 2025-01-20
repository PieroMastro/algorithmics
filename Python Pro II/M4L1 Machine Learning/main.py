import pandas as pd

# EXTRACCION
df = pd.read_csv('titanic.csv')
# print(df.info())
# print(df.head())

# COMPROBANDO HIPOTESIS
print(df.groupby(by='Sex')['Survived'].mean())

table = df.pivot_table(
    index = 'Survived',
    columns= 'Pclass',
    values= 'Age',
    aggfunc= 'mean'
)
print(table)

# PREPARACION
#1. Eliminar columnas que no tienen utilidad para nuestro modelo
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

#2. Reemplazar valores nulos
#2.1 Puerto de embarque
print(df['Embarked'].value_counts())
df['Embarked'].fillna('S', inplace=True)

#2.2 Edad
print(df.groupby(by='Pclass')['Age'].median())
age_1 = df[df['Pclass'] == 1]['Age'].median()
age_2 = df[df['Pclass'] == 2]['Age'].median()
age_3 = df[df['Pclass'] == 3]['Age'].median()

def replace_age(row):
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age_1
        if row['Pclass'] == 2:
            return age_2
        return age_3
    return row['Age']

df['Age'] = df.apply(replace_age, axis=1)

#3. Conversion de objetos a datos numericos
#3.1 Genero
def replace_gender(gender):
    if gender == 'male':
        return 1
    return 0

df["Sex"] = df['Sex'].apply(replace_gender)
print(df.info())

#3.2 Crear variables dummies para reeemplazar los valores categoricos
print(pd.get_dummies(df['Embarked']))
df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])
df.drop('Embarked', axis=1, inplace=True)
print(df.head())

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


