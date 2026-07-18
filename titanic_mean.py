import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('titanic.csv')
print(data.head(5))
mean_age = np.mean(data['Age'])
print("Average age of passenger is:", mean_age)

mean_fare = np.mean(data['Fare'])
print("Average fare cost of passenger is:", mean_fare)