import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append('C:/Users/Чигин Сергей/Desktop/mplstyle/')

from mplstyle.tz import PLTtz

tz_plt = PLTtz()

fig1 = plt.figure(figsize=[8, 6])
fig2 = plt.figure(figsize=[8, 6])

# 1st plot
#########
ax0 = fig1.add_subplot(211)

# setting four trigonometric functions
x = np.arange(0, 2 * np.pi, 0.01)
for c in range(4):
    y = np.sin(x) + c
    ax0.plot(x, y, label=c)

# labeling axises, putting legend and title
ax0.set_title('plot #1 (default - default - default)')
ax0.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
ax0.set_xlabel(r'Power ($kW$)')
ax0.legend()

# 2nd plot
#########
# changing all plot settings
tz_plt.set_style(color_style='mpl2_colors')
tz_plt.set_style(color_order_style='mpl2_colors')
tz_plt.set_style(plt_style='jupyter-notebook')

ax1 = fig1.add_subplot(212)

x1 = np.arange(0, 2 * np.pi, 0.01)
for c1 in range(4):
    y1 = np.sin(x1) + c1
    ax1.plot(x1, y1, label=c1)

ax1.set_title('plot #2 (mpl2_colors - mpl2_colors - jupyter-notebook)')
ax1.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
ax1.set_xlabel(r'Power ($kW$)')
ax1.legend()

fig1.tight_layout()
plt.show()



# 3rd plot
#########
# changing only plt_style setting
tz_plt.set_style(plt_style='default')

ax2 = fig2.add_subplot(211)

x2 = np.arange(0, 2 * np.pi, 0.01)
for c2 in range(4):
    y2 = np.sin(x2) + c2
    ax2.plot(x2, y2, label=c2)

ax2.set_title('plot #3 (mpl2_colors - mpl2_colors - default)')
ax2.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
ax2.set_xlabel(r'Power ($kW$)')
ax2.legend()

# 4rth plot
#########
# changing all plot settings with one function
tz_plt.set_style('default')

ax3 = fig2.add_subplot(212)

x3 = np.arange(0, 2 * np.pi, 0.01)
for c3 in range(4):
    y3 = np.sin(x3) + c3
    ax3.plot(x3, y3, label=c3)

ax3.set_title('plot #4 (default - default - default)')
ax3.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
ax3.set_xlabel(r'Power ($kW$)')
ax3.legend()


fig2.tight_layout()
plt.show()
