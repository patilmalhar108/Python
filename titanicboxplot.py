import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('titanic.csv')
print(data.head(5))
print(data.isnull().sum())

plt.boxplot(data['Age'])
plt.title("Age distribution")
plt.show()

plt.boxplot(data['Pclass'])
plt.title("Passenger Class distribution")
plt.show()