import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# add dir mplstyle to python path
sys.path.append(os.path.split(os.path.dirname(os.getcwd()))[-2])
from mplstyle.ewk import PLTewk


def color_map_example():
    """ An example of how to use get_cmap."""
    ewk_plt.set_style('default')
    fig = plt.figure(figsize=(14, 12))
    fig.suptitle('Define your own color maps', fontsize=20, fontweight='bold')
    fig.subplots_adjust(hspace=0.3, top=0.91)

    ax0 = fig.add_subplot(311)
    colors = [(21, 71, 157), (53, 117, 227), (210, 224, 249)]
    plt.pcolor(np.random.rand(25, 50), cmap=ewk_plt.get_cmap(colors, bit=True))
    plt.colorbar()
    ax0.set_title('default style')

    ax1 = fig.add_subplot(312)
    ewk_plt.set_style('example')
    ewk_colors = ewk_plt.get_colors()
    colors = [ewk_colors['lightred'], ewk_colors['mdarkred']]
    plt.pcolor(np.random.rand(25, 50), cmap=ewk_plt.get_cmap(colors))
    plt.colorbar()
    ax1.set_title('example style: red color')

    ewk_plt.set_style('ewk')
    ax2 = fig.add_subplot(313)
    colors = [(0.4, 0.2, 0.0), (1, 1, 1), (1, 1, 0), (0, 0.3, 0.4)]
    position = [0, 0.2, 0.5, 1]
    plt.pcolor(np.random.rand(25, 50),
               cmap=ewk_plt.get_cmap(colors, position=position))
    plt.colorbar()
    ax2.set_title('enfo style')

    ewk_plt.add_zbild(ax2, xloc=.82, yloc=1.02, text='88-xxx-B16')
    plt.show()


if __name__ == "__main__":
    ewk_plt = PLTewk()
    color_map_example()
