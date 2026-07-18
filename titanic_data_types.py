import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data = pd.read_csv('titanic.csv')
print(data.head(5))
print(data['Survived'].dtypes)
data.isnull().sum()