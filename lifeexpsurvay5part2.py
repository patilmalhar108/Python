# Import Libraries and Dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Read the CSV file
data = pd.read_csv('gapminder(2007).csv')
# Display first 5 rows
print(data.head())
# Display column names
print(data.columns)
# Group by continent and calculate mean of life expectancy
grouped_df = data.groupby('continent', as_index=False)['life_exp'].mean()
print(grouped_df)
# Create the figure
plt.figure(figsize=(8,5))
# Draw the bar plot
plots = sns.barplot(
data=grouped_df,
x='continent',
y='life_exp',
color='teal'
)
# Annotate each bar
for bar in plots.patches:
    height = bar.get_height()
    plots.annotate(
    f'{height:.2f}',
    xy=(bar.get_x() + bar.get_width()/2, height),
    xytext=(0, 5),
    textcoords='offset points', # Correct syntax
    ha='center',
    va='bottom',
    fontsize=11
    )
# Labels and title
plt.xlabel("Continents", fontsize=12)
plt.ylabel("Life Expectancy", fontsize=12)
plt.title("Average Life Expectancy by Continent", fontsize=14)
plt.tight_layout()
plt.show()