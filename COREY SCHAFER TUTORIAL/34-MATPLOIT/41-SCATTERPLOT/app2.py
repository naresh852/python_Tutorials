#scatter plots are great when you want to show relation between two sets of values and see if they are corelated
#Matplotlib Marker Styles - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# Matplotlib Colormaps-https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']
plt.scatter(view_count,likes,c=ratio,cmap='summer',edgecolors='yellow',linewidths=1,alpha=0.75)
cbar=plt.colorbar()
cbar.set_label('likes dislikes ratio')
plt.xscale('log')
plt.yscale('log')

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()