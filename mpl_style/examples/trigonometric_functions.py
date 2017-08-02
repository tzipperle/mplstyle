import matplotlib.pyplot as plt
import numpy as np
import os
import sys

sys.path.append(os.path.split(os.path.dirname(os.getcwd()))[-2])

from mpl_style.PLT_tz import PLTtz
tz_plt=PLTtz()


fig = plt.figure(figsize=[8,9])

#1st plot
#########
ax0 = fig.add_subplot(311)

#setting four trigonometric functions
x = np.arange(0, 2 * np.pi, 0.01)
for c in range(4):
    y = np.sin(x) + c
    ax0.plot(x, y, label=c)

#labeling axises, putting legend and title 
ax0.set_title('default - default - default')
ax0.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
ax0.set_xlabel(r'Power ($kW$)')
ax0.legend()

#2nd plot
#########
#changing all plot settings
tz_plt.set_style(color_style='mpl2_colors')
tz_plt.set_style(color_order_style='mpl2_colors')
tz_plt.set_style(plt_style='jupyter-notebook')

ax1 = fig.add_subplot(312)

x1 = np.arange(0, 2 * np.pi, 0.01)
for c1 in range(4):
    y1 = np.sin(x1) + c1
    ax1.plot(x1, y1, label=c1)

ax1.set_title('mpl2_colors - mpl2_colors - jupyter-notebook')
ax1.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
ax1.set_xlabel(r'Power ($kW$)')
ax1.legend()

#3rd plot
#########
#changing all plot settings
tz_plt.set_style(plt_style='default')

ax2 = fig.add_subplot(313)

x2 = np.arange(0, 2 * np.pi, 0.01)
for c2 in range(4):
    y2 = np.sin(x2) + c2
    ax2.plot(x2, y2, label=c2)

ax2.set_title('mpl2_colors - mpl2_colors - default')
ax2.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
ax2.set_xlabel(r'Power ($kW$)')
ax2.legend()

fig.tight_layout()
plt.show()