import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statistics as stats
data = pd.read_csv('titanic.csv')
print(data.head(5))
median_age = np.median(data['Age'])
print('The middle centered age of sorted list is:', median_age)

median_fare = np.median(data['Fare'])
print('The middle centered fare of sorted list is:', median_fare)

mode_age = stats.mode(data['Age'])
print('The most frequant age of list is:', mode_age)

mode_pclass = stats.mode(data['Pclass'])
print('The most frequant class of the list is:', mode_pclass)

mode_gender = data['Gender'].value_counts().index[0]
print('The most frequant gender of the list is:', mode_gender)