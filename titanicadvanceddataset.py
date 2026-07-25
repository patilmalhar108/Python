import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('titanic.csv')
print(data.head())
min_age = data['Age'].min()
print("Minimum age is equal to:", min_age)
max_age = data['Age'].max()
print("Maximum age is =", max_age)
bins = [0,15,30,45,60,75]
data['bin_age'] = pd.cut(data['Age'], bins)
print(data[['bin_age', 'Age']].head())
age_labels = ['young', 'young-adult', 'middle aged', 'middle older age', 'senior']
data['bin_age'] = pd.cut(data['Age'], bins, labels = age_labels)
data['bin_age'].value_counts().plot(kind = 'bar')
plt.title("Dance class age distribution")
plt.xlabel("Ages")
plt.ylabel("Count")
labels = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
for label in labels:
    print('Distribution of', label)
    sns.distplot(data[label])
    plt.show()
    print("Skewness:", data[label].skew())

data['log_SibSp'] = np.log(data['SibSp'])
data['log_Parch'] = np.log(data['Parch'])
data['log_Fare'] = np.log(data['Fare'])