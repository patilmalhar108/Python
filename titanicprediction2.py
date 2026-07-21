import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('titanic.csv')
print(data.head(5))
print(data.isnull().sum())

age_Q1 = np.quantile(data['Age'], 0.25)
age_Q2 = np.quantile(data['Age'], 0.25)
age_Q3 = np.quantile(data['Age'], 0.25)

print("Age quartile:")
print("Q1 =", age_Q1)
print("Q2 =", age_Q2)
print("Q3 =", age_Q3)

IQR_age = (age_Q3 - age_Q1)
print("Inter quartile range =", IQR_age)

plt.hist(data['Age'])
plt.ylabel("Count of passengers")
plt.xlabel("Age")
plt.show()

fare_Q1 = np.quantile(data['Fare'], 0.25)
fare_Q2 = np.quantile(data['Fare'], 0.25)
fare_Q3 = np.quantile(data['Fare'], 0.25)
print("Fare quartile:")
print("Q1 =", fare_Q1)
print("Q2 =", fare_Q2)
print("Q3 =", fare_Q3)

IQR_fare = (fare_Q3 - fare_Q1)
print("Inter quartile range =", IQR_fare)

plt.hist(data['Fare'])
plt.ylabel("Count of passengers")
plt.xlabel("Fare")
plt.show()