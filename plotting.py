## Plotting options in matplotli/seaborn

# Imports and settings
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
plt.style.use('seaborn-whitegrid')
pd.set_option('display.max_columns', 100)

import matplotlib.ticker as ticker
import matplotlib.dates as mdates

# start plot
fig, ax = plt.subplots(figsize = (20,7))

# set title
ax.set_title(f'Title')

#plot
sns.lineplot(x = 'x', y = 'y', data = df, label = 'label', color = 'black', alpha = 0.6, ax= ax) #, marker = 'o', markersize = 2
#...more lineplots

#set line style for one of lineplot
ax.lines[2].set_linestyle("--")

#set axis label
ax.set_xlabel('x-label');ax.set_ylabel('y-label')

# set all values in x tick
ax.set_xticks(df.date.values) #or ax.set(xticks=df.x.values) 

# set rotation
ax.set_xticklabels(ax.get_xticklabels(), rotation=45) #or plt.xticks(rotation = 45);
 
# to space ticks linearly
ax.xaxis.set_major_locator(ticker.LinearLocator()) 

#Show when in year to show the tick
ax.xaxis.set_major_locator(mdates.YearLocator(1))
# ax.xaxis.set_major_locator(ticker.MultipleLocator(240))

#format the format of ticker to specific date example
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y')) 

#set grip alpha
ax.grid(alpha = 0.5)

# modify legend
ax.legend(loc = 'upper left', fontsize = 'large', handlelength = 4, frameon = True, fancybox = True, shadow = True, framealpha = 0.95) #, title = 'Legend', title_fontsize = 'large'
