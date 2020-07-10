from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# User input
country = input("Enter Region: ")

# Loading and cleaning dataframe
df = pd.read_csv('inflation.csv')
df = df.drop(['Indicator Name', 'Indicator Code', 'Unnamed: 64'], axis=1)
df = df[df['Country Name'].values == country]
df = df.drop(['Country Name', 'Country Code'], axis=1)
df = df.dropna(axis=1)

# Creating an array for present values every year
data = np.array(df.iloc[0])
pv = []
pv.append(1)
for i in range(1, len(data) + 1):
    pv.append((1 + 0.01 * data[i - 1]) * pv[i - 1])
print(pv)
# Visualising data
ax = plt.subplot()
plt.plot(range(len(pv)), pv, color = 'red', marker='o', markersize=4)
plt.xlabel('Years after ' + df.columns[0])
plt.ylabel("Value of 1 unit of {country}'s currency (relative to {start})".format(country=country, start=df.columns[0]))
ax.yaxis.set_major_locator(plt.MaxNLocator(20))
plt.title(country + '\'s Time Value of Money')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
plt.grid()
plt.show()
plt.clf()
