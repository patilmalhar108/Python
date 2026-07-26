import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv('iris.csv')
print(data.head())
print(data.isnull().sum())
print(data.describe())
labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
for label in labels:
    print("Distribution of", label)
    sns.boxplot(data[label])
    plt.show()

sns.heatmap(data.corr())
labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
for label in labels:
    print("Distribution of", label)
    sns.distplot(data[label])
    plt.show()

labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
for label in labels:
    print("Skewness of", label)
    print(data[label].skew())