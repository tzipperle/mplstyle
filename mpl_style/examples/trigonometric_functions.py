import matplotlib.pyplot as plt
import numpy as np
import os
import sys

sys.path.append(os.path.split(os.path.dirname(os.getcwd()))[-2])

from mpl_style.PLT_tz import PLTtz
tz_plt=PLTtz()


fig = plt.figure(figsize=[8,6])
ax0 = fig.add_subplot(211)

x = np.arange(0, 2 * np.pi, 0.01)
for c in range(4):
    y = np.sin(x) + c
    ax0.plot(x, y, label=c)

ax0.set_title('default - default - default')
ax0.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
ax0.set_xlabel(r'Power ($kW$)')
ax0.legend()


tz_plt.set_style(color_style='mpl2_colors')
tz_plt.set_style(color_order_style='mpl2_colors')
tz_plt.set_style(plt_style='default')

ax1 = fig.add_subplot(212)

x1 = np.arange(0, 2 * np.pi, 0.01)
for c1 in range(4):
    y1 = np.sin(x1) + c1
    ax1.plot(x1, y1, label=c1)

ax1.set_title('mpl2_colors - mpl2_colors - jupyter-notebook')
ax1.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
ax1.set_xlabel(r'Power ($kW$)')
ax1.legend()




fig.tight_layout()
    
plt.show()