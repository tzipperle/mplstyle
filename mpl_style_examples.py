import numpy as np
import matplotlib.pyplot as plt
from mpl_style_ewk import EWKPlot


def example():
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

    ewk_plt.add_zbild(ax, xloc=0.005, yloc=0.01, zbild='88-xxx-B16')
    plt.tight_layout()
    plt.show()
    return


def example_and_default():
    ewk_plt.set_all_style('default')
    fig = plt.figure()
    ax0 = fig.add_subplot(221)

    x = np.arange(0, 2 * np.pi, 0.01)
    for c in range(4):
        y = np.sin(x) + c
        ax0.plot(x, y, label=c)

    ax0.set_title('Default style')
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

    ewk_plt.set_all_style('example')
    ax2 = fig.add_subplot(222)
    for c in range(4):
        y = np.sin(x) + c
        ax2.plot(x, y, label=c)

    ax2.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
    ax2.set_xlabel(r'Power ($kW$)')
    ax2.set_title('Example style')
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


def color_map_example():
    """ An example of how to use get_cmap."""
    ewk_plt.set_all_style('default')
    fig = plt.figure(figsize=(14, 12))
    fig.suptitle('Define your own color maps', fontsize=20, fontweight='bold')
    fig.subplots_adjust(hspace=0.3, top=0.91)

    ax0 = fig.add_subplot(311)
    colors = [(21, 71, 157), (53, 117, 227), (210, 224, 249)]
    plt.pcolor(np.random.rand(25, 50), cmap=ewk_plt.get_cmap(colors, bit=True))
    plt.colorbar()
    ax0.set_title('Default style')

    ax1 = fig.add_subplot(312)
    ewk_colors = ewk_plt.get_colors()
    colors = [ewk_colors['lightred'], ewk_colors['mdarkred']]
    plt.pcolor(np.random.rand(25, 50), cmap=ewk_plt.get_cmap(colors))
    plt.colorbar()
    ax1.set_title('Default style: red color')

    ewk_plt.set_all_style('example')
    ax2 = fig.add_subplot(313)
    colors = [(0.4, 0.2, 0.0), (1, 1, 1), (1, 1, 0), (0, 0.3, 0.4)]
    position = [0, 0.2, 0.5, 1]
    plt.pcolor(np.random.rand(25, 50),
               cmap=ewk_plt.get_cmap(colors, position=position))
    plt.colorbar()
    ax2.set_title('Example style')

    ewk_plt.add_zbild(ax2, xloc=.82, yloc=1.02, zbild='88-xxx-B16')
    plt.show()


if __name__ == "__main__":
    ewk_plt = EWKPlot()
    example()
    ewk_plt.set_all_style(style='example', enable_color_order=True)
    example()
    example_and_default()
    color_map_example()
