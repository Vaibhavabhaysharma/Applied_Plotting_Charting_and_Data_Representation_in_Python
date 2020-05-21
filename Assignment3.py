
import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df

import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
%matplotlib notebook

df_mean = df.mean(axis=1) # Averaging column entries.

# df.shape[1] gives the number of columns = 3650.
# df.std only does numerator calculation of standard deviation formula.
df_std = df.std(axis=1)/np.sqrt(df.shape[1])

# Choice of y value:
y = 37000

# In probability and statistics, 1.96 is the approximate value of the 97.5 percentile point of the normal distribution.
# 95% of the area under a normal curve lies within roughly 1.96 standard deviations of the mean, and due to the central limit theorem, this number is therefore used in the construction of approximate 95% confidence intervals.
norm = Normalize(vmin=-1.96, vmax=1.96)

# 'seismic', 'coolwarm', etc. are examples of available colour palettes.
cmap = get_cmap('coolwarm')

df_colors = pd.DataFrame([])
df_colors['intensity'] = norm((df_mean-y)/df_std) # Usual normalising formula.
df_colors['color'] = [cmap(x) for x in df_colors['intensity']] # Assign colour depending on norm value.

# Remember we normalised df_std for assigning colour intensity earlier. Therefore the actual error will be scaled by 1.96.
# capsize sets thw whiskers for the error on the barplot.
bar_plot = plt.bar(df.index, df_mean, yerr=df_std*1.96, color=df_colors['color'], capsize=7);

# axhline = Horizontal line.
hoz_line = plt.axhline(y=y, color='k', linewidth=2, linestyle='--');

# Text box for chosen value. 1995.5 gives the x axis location for positioning the box.
# ec is the colour of the box border. fc is the colour of the box filling.
y_text = plt.text(1995.45, y, 'y = %d' %y, bbox=dict(fc='white',ec='k'));

# Add xticks
plt.xticks(df.index, ('1992', '1993', '1994', '1995'));

# Add interactivity
def onclick(event):
    for i in range(4):
        shade = cmap(norm((df_mean.values[i]-event.ydata)/df_std.values[i]))
        bar_plot[i].set_color(shade) 
    hoz_line.set_ydata(event.ydata)
    y_text.set_text('y = %d' %event.ydata);
    y_text.set_position((1995.45, event.ydata));
    
plt.gcf().canvas.mpl_connect('button_press_event', onclick);
