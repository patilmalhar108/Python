import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('weather.csv')
print(data.info())
print(data.isnull().sum())

mean_temp = np.mean(data['Temperature (C)'])
print("The average temperature is:", mean_temp)

var_temp = np.var(data['Temperature (C)'])
print("The temperature variance is:", var_temp)

standerd_dev = np.std(data['Temperature (C)'])
print("The standerd deveation of temperature is:", standerd_dev)

for i in range(1, 13):
    month = data.loc[data["month"] == i]["Temperature (C)"]
    print("For Month", i)
    print("Average Temperature:", np.mean(month))
    print("Variance:", np.var(month))
    print("Standard Deviation:", np.std(month))
    print()