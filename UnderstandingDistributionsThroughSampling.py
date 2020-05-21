import matplotlib.pyplot as plt
import numpy as np

%matplotlib notebook

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

# plot the histograms
plt.figure(figsize=(9,3))
plt.hist(x1, normed=True, bins=20, alpha=0.5)
plt.hist(x2, normed=True, bins=20, alpha=0.5)
plt.hist(x3, normed=True, bins=20, alpha=0.5)
plt.hist(x4, normed=True, bins=20, alpha=0.5);
plt.axis([-7,21,0,0.6])

plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')

import matplotlib.animation as animation

ti = ['normal','gamma','exponential','uniform']

x = [x1,x2,x3,x4]

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharex = True,sharey =True)
ax = [ax1,ax2,ax3,ax4]


val = 0

def update(curr):
    global val
    if val == 50:
        a.event_source.stop()
    
    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()
    num = np.random.randint(100,1000)
    ax1.hist(x1[:num], normed=True, bins= 30)
    ax2.hist(x2[:num],normed=True, bins= 30)
    ax3.hist(x3[:num],normed=True, bins= 30)
    ax4.hist(x4[:num],normed=True, bins= 30)
    
    for i in range(0,len(ax)):
        ax[i].set_title(ti[i])
    ax1.tick_params(axis="x", which='both', bottom =False, top= False)
    ax2.tick_params(axis="x", which='both', bottom =False, top= False)
    ax1.get_xaxis().set_visible(False)
    ax2.get_xaxis().set_visible(False)
    val = val+1
    ax1.axis([-7,21,0,0.6])
    

a = animation.FuncAnimation(fig, update, interval=100)
plt.show()
