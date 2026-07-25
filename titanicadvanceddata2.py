import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
data = pd.read_csv('titanic.csv')
print(data.head(5))
sns.boxplot(data = data, x = 'Embarked', y = 'Age')
plt.show()

plt.scatter(x = data['Fare'], y = data['Survived'])
plt.ylabel('Survived')
plt.xlabel("Fare")
plt.show()

plt.scatter(x = data['Parch'], y = data['Survived'])
plt.ylabel("Survived")
plt.xlabel("Parch")
plt.show()

plt.scatter(x = data['SibSp'], y = data['Survived'])
plt.ylabel("Survived")
plt.xlabel("SibSp")
plt.show()

association_catagorical = pd.crosstab(data['Gender'], data['Embarked'])
print(association_catagorical)