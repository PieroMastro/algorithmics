import pandas as pd

df = pd.read_csv('train.csv')

# bdate es importante (year), pero debemos configurar una nueva caracteristica para ello e incorporarla en la df 

df.drop(['id', 'bdate', 'has_mobile', 'langs', 'city', 'occupation_name', 'people_main', 'relation'], axis=1, inplace=True)
df['occupation_type'].fillna('university', inplace=True)
df['education_form'].fillna('Full-time', inplace=True)

print(df.info())
print(df['education_form'].value_counts())

df[list(pd.get_dummies(df['education_form']).columns)] = pd.get_dummies(df['education_form'])
df.drop('education_form', axis=1, inplace=True)

df[list(pd.get_dummies(df['life_main']).columns)] = pd.get_dummies(df['life_main'])
df.drop('life_main', axis=1, inplace=True)

print(df.info())
