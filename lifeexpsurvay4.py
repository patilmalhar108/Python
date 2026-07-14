import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('gapminder(2007).csv')
print(data.head())
print(data.isnull().any())
print(data.info())

sns.set_style('white')
sns.countplot(x = data['continent'])
plt.show()

sns.set_style('dark')
sns.countplot(x = data['continent'])
plt.show()

sns.set_style('whitegrid')
sns.countplot(x = data['continent'])
plt.show()

sns.set_style('darkgrid')
sns.countplot(x = data['continent'])
plt.show()

sns.set_style('ticks')
sns.countplot(x = data['continent'])
plt.show()

sns.set_style('white')
sns.countplot(x = data['continent'])
sns.despine()
plt.show()

sns.set_style('ticks')
sns.countplot(x = data['continent'], palette = 'winter')
plt.show()

sns.set_style('ticks')
sns.countplot(x = data['continent'], color = 'purple')
plt.show()

sns.set_style('ticks')
sns.countplot(x = data['continent'], color = 'purple')
sns.set_context('paper')
plt.show()

sns.set_style('ticks')
sns.countplot(x = data['continent'], color = 'purple')
sns.set_context('talk')
plt.show()

sns.set_style('ticks')
sns.countplot(x = data['continent'], color = 'purple')
sns.set_context('notebook')
plt.show()

sns.set_style('ticks')
sns.countplot(x = data['continent'], color = 'purple')
sns.set_context('poster')
plt.xticks(rotation = 45)
plt.show()

sns.set_style('whitegrid')
sns.set_context('poster', font_scale = 0.8)
sns.countplot(x = data['continent'], color = 'purple')
plt.xticks(rotation = 45)
plt.show()