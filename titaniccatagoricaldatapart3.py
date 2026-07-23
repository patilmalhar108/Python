import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('titanic.csv')
print(data.head(5))
num_data = data.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'Gender'], axis = 1)
labels = ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
for label in labels:
    plt.boxplot(num_data[label])
    print("Distribution of ",label)
    plt.show()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
num_data = scaler.fit_transform(num_data)