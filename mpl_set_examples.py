import numpy as np
import matplotlib.pyplot as plt
from mpl_set_ewk import EWKPlot


def example_1():
    colors = ewk_plt.get_colors()
    c_order = ewk_plt.get_order()

    x = [0, 1]
    ax = plt.subplot()

    for i, c in enumerate(c_order):
        y = [len(c_order) - i] * 2
        ax.plot(x, y, color=colors[c])

    ax.set_yticks(range(1, len(colors) + 1))
    ax.set_yticklabels(c_order[::-1])
    ax.set_xticklabels([])
    ax.grid(False)
    ewk_plt.add_zbild(ax, xloc=0.005, yloc=0.01, zbild='88-xxx-B16')
    plt.tight_layout()
    plt.show()
    return


def example_2():
    fig = plt.figure()
    ax = fig.add_subplot(211)

    x = np.arange(0, 2 * np.pi, 0.01)
    for c in range(4):
        y = x * 0 - c
        ax.plot(x, y, label=c)

    ax.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
    ax.set_xlabel(r'Power ($kW$)')
    ax.legend()

    ax = fig.add_subplot(212)
    x = np.arange(0, 2 * np.pi, 0.01)
    for c in range(7):
        y = x * 0 - c
        ax.plot(x, y, label=c)

    ax.set_ylabel(r'electric Power ($\mathrm{kW}$)')
    ax.set_xlabel(r'Power ($kW$)')
    ax.legend()
    ewk_plt.add_zbild(ax, xloc=0.83, yloc=1.02, zbild='88-xxx-B16',
                      fontsize=10)
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    ewk_plt = EWKPlot()
    example_2()
    example_1()

    ewk_plt.set_all_style('example')
    example_1()

