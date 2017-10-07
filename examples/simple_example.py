import matplotlib.pyplot as plt
import numpy as np
from mplstyle.ewk import PLTewk


def plt_color_order(title):
    colors = ewk_plt.get_colors()
    c_order = ewk_plt.get_color_order()

    x = [0, 1]
    fig, ax = plt.subplots()
    for i, c in enumerate(c_order):
        y = [len(c_order) - i] * 2
        ax.plot(x, y, color=colors[c])

    ax.set_yticks(range(1, len(colors) + 1))
    ax.set_yticklabels(c_order[::-1])
    ax.set_xticklabels([])
    ax.set_title(title)

    ewk_plt.add_zbild(ax=ax, x=0.005, y=0.01, text='88-000-B17')
    plt.tight_layout()
    plt.show()


def simple_subplot():
    def plt_sin(ax):
        x = np.arange(0, 2 * np.pi, 0.01)
        for c in range(4):
            y = np.sin(x) + c
            ax.plot(x, y, label=c)

    def plt_const(ax):
        x = np.arange(0, 2 * np.pi, 0.01)
        for c in range(6):
            y = x * 0 + c
            ax.plot(x, y, label=c)

    ewk_plt.set_style('ewk')
    fig = plt.figure()
    ax0 = fig.add_subplot(221)

    plt_sin(ax0)
    ax0.set_title('ewk style')
    ax0.legend()

    ax1 = fig.add_subplot(223)
    plt_const(ax1)
    ax1.legend()

    ewk_plt.set_style('ewk_ggplt')
    ax2 = fig.add_subplot(222)
    plt_sin(ax2)
    ax2.set_title('ewk_ggplt style')
    ax2.legend()

    ax3 = fig.add_subplot(224)
    plt_const(ax3)
    ax3.legend()

    ewk_plt.add_zbild(ax=ax3, x=0.73, y=1.02, text='88-001-B17',
                      fontsize=8)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    ewk_plt = PLTewk()
    ewk_plt.set_style(plt_style='ewk_ggplt')
    ewk_plt.get_available_styles()
    plt_color_order(title='default style')
    simple_subplot()
