import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, accuracy_score

# TRAIN DF
df = pd.read_csv('train.csv')
df.drop(['id','bdate','graduation', 'education_status',
        'last_seen', 'city','occupation_name', 'career_start',
        'career_end','langs', 'people_main'], axis=1, inplace= True)

df['education_form'].fillna('Full-time', inplace= True)
df['occupation_type'].fillna('university', inplace = True)

def replace_false(data):
    if data=='False':
        return int(9)
    else:
        return int(data)
df['life_main'] = df['life_main'].apply(replace_false)

def change_occupation(data):
    if data == 'university':
        return 1
    return 0
df['occupation_type'] = df['occupation_type'].apply(change_occupation)

df[list(pd.get_dummies(df['education_form']).columns)] = pd.get_dummies(df['education_form'])
df.drop('education_form', axis=1, inplace=True)


x = df.drop('result', axis=1)
y = df['result']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# MODEL 1 SET
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)
y_predict = classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_predict) * 100
print(f'Porcentaje de acierto (KNN): {round(accuracy, 2)}%')

# MODEL 2 (Decision Tree)
clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

score = clf.score(x_test, y_test) * 100
print(f"Porcentaje de acierto (CTree): {round(score, 2)}%")


plt.figure(figsize=(10, 5))
plot_tree(clf, filled=True, feature_names=x.columns, class_names=['0', '1'])
plt.show()

