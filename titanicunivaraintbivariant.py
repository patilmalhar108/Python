import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('titanic.csv')
print(data.head(5))
sns.countplot(x = 'Gender', hue = 'Survived', data = data)
plt.show()
sns.countplot(x = 'Pclass', hue = 'Survived', data = data)
plt.show()
sns.distplot(data['Age'], kde = False, bins = 40)
plt.show()
sns.countplot(data['Gender'])
plt.show()
sns.countplot(x = 'Survived', hue = 'Parch', data = data, palette = 'mako')
sns.distplot(data['Fare'])
plt.show()
sns.boxplot(x = 'Pclass', y = 'Age', data = data, palette = 'winter')
sns.heatmap(data.corr())