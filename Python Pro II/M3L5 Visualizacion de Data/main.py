import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(data = [10, 5, 15, 20, 10],
    index = [1, 2, 3, 4, 5])
s.plot()
plt.show()

df = pd.read_csv ('Python Pro II/M3L5 Visualizacion de Data/GoogleApps.csv')
print(df.info())

# Histograma de tamaños de aplicaciones
df['Size'].plot(kind = 'hist')

df['Size'].plot(kind = 'hist', bins = 5)

df[df['Type'] == 'Paid']['Price'].plot(kind = 'hist')
