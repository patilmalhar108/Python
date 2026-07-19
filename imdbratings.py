import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('imdb.csv')
print(data.head(5))

plt.hist(data['Runtime'])
plt.ylabel("Count of Movies")
plt.xlabel("Run Time")
plt.show()

plt.hist(data['IMDB_Rating'])
plt.ylabel("Count of Movies")
plt.xlabel("IMDB Ratings")
plt.show()

data["Runtime"].unique()
bins_time = np.arange(80,230,10)
plt.hist(data['Runtime'], edgecolor = 'black', bins = bins_time, color = 'g')
plt.ylabel("Conut of Movies")
plt.xlabel("Runtime")
plt.show()

data["IMDB_Rating"].unique()
bins_rating = np.arange(8,10,0.2)
plt.hist(data['IMDB_Rating'], edgecolor = 'black', bins = bins_rating, color = 'g')
plt.ylabel("Count of Movies")
plt.xlabel("IMDB Rating")
plt.show()

plt.xticks(bins_rating)