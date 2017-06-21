import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# add dir mpl_style to python path
sys.path.append(os.path.split(os.path.dirname(os.getcwd()))[-2])
from mpl_style.style_ewk import PLTewk


def plt_color_order(title):
    colors = ewk_plt.get_colors()
    c_order = ewk_plt.get_color_order()

    x = [0, 1]
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for i, c in enumerate(c_order):
        y = [len(c_order) - i] * 2
        ax.plot(x, y, color=colors[c])

    ax.set_yticks(range(1, len(colors) + 1))
    ax.set_yticklabels(c_order[::-1])
    ax.set_xticklabels([])
    ax.grid(True)
    ax.set_title(title)

    ewk_plt.add_zbild(ax, xloc=0.005, yloc=0.01, zbild='88-xxx-B16')
    plt.tight_layout()
    plt.show()
    return


def simple_subplot():
    ewk_plt.set_style('ewk')
    fig = plt.figure()
    ax0 = fig.add_subplot(221)

    x = np.arange(0, 2 * np.pi, 0.01)
    for c in range(4):
        y = np.sin(x) + c
        ax0.plot(x, y, label=c)

    ax0.set_title('ewk style')
    ax0.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
    ax0.set_xlabel(r'Power ($kW$)')
    ax0.legend()

    ax1 = fig.add_subplot(223)

    for c in range(6):
        y = x * 0 + c
        ax1.plot(x, y, label=c)

    ax1.set_ylabel(r'electric Power ($\mathrm{kW}$)')
    ax1.set_xlabel(r'Power ($kW$)')
    ax1.legend()

    ewk_plt.set_style(color_order_style='default', color_style='default',
                      plt_style='example')
    ax2 = fig.add_subplot(222)
    for c in range(4):
        y = np.sin(x) + c
        ax2.plot(x, y, label=c)

    ax2.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
    ax2.set_xlabel(r'Power ($kW$)')
    ax2.set_title('example style')
    ax2.legend()

    ax3 = fig.add_subplot(224)

    for c in range(6):
        y = x * 0 + c
        ax3.plot(x, y, label=c)

    ax3.set_ylabel(r'electric Power ($\mathrm{kW}$)')
    ax3.set_xlabel(r'Power ($kW$)')
    ax3.legend()

    ewk_plt.add_zbild(ax3, xloc=0.7, yloc=1.02, zbild='88-xxx-B16',
                      fontsize=10)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    ewk_plt = PLTewk()
    ewk_plt.get_available_styles()
    # plt_color_order(title='default style')
    simple_subplot()
