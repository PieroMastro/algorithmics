import pandas as pd

# EXTRACCION
df = pd.read_csv('titanic.csv')
# print(df.info())
# print(df.head())

# COMPROBANDO HIPOTESIS
# print(df.groupby(by='Sex')['Survived'].mean())

table = df.pivot_table(
    index = 'Survived',
    columns= 'Pclass',
    values= 'Age',
    aggfunc= 'mean'
)
# print(table)

# PREPARACION
#1. Eliminar columnas que no tienen utilidad para nuestro modelo
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

#2. Reemplazar valores nulos
#2.1 Puerto de embarque
# print(df['Embarked'].value_counts())
df['Embarked'].fillna('S', inplace=True)

#2.2 Edad
# print(df.groupby(by='Pclass')['Age'].median())
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
# print(df.info())

#3.2 Crear variables dummies para reeemplazar los valores categoricos
# print(pd.get_dummies(df['Embarked']))
df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])
df.drop('Embarked', axis=1, inplace=True)
# print(df.head())

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# SETTING UP THE MODEL
# 1. Imports
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

# 2. Dividir la muestra en las 2 variables
x = df.drop('Survived', axis=1)
y = df['Survived']

# 3. Separar la muestra en 2 grupos, train y test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# 4. Estandarizacion de metricas
# 4.1 Instancia de la clase StandardScaler
sc = StandardScaler()

# 4.2 Remplazar los valores al rango establecido
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# 5. Creacion del modelo
classifier = KNeighborsClassifier(n_neighbors=5)

# 6. Entrenamiento del modelo
classifier.fit(x_train, y_train)

# 7. Pruebas
y_predict = classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_predict, normalize=True) * 100
print(f'Porcentaje de acierto: {round(accuracy, 2)}%')
