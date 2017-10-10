import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mplstyle.base import PLTbase


def plot_3d():
    # read data
    df = pd.read_csv('data/3D_example_data.csv')

    # create colormap for 3D plot
    cc = base_style.get_colors()
    cmap = base_style.get_cmap(
        [cc['lightblue'], cc['mlightblue'], cc['mediumblue'],
         cc['mdarkblue'], cc['darkblue']],
        [0, 0.1, 0.2, 0.5, 1])

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x, y = np.meshgrid(df.q_ch, df.q_dch)
    X, Y = np.meshgrid(df.E_ch, df.E_dch)
    eff = Y / X * 100

    ax.plot_surface(x, y, eff, rstride=1, cstride=1, cmap=cmap, linewidth=0,
                    antialiased=False)

    ax.set_xlim(0, 1.5)
    ax.set_ylim(0, 2)
    ax.set_zlim(50, 100)

    ax.set_xticks(np.arange(0, 1.5, 0.3))
    ax.set_yticks(np.arange(0, 1.8, 0.3))

    ax.set_xlabel(
        '\n\n' + r'Air demand charging ($\frac{\mathrm{m}^3'
                 r'_{\mathrm{n}}}{\mathrm{min}}$)')
    ax.set_ylabel(
        '\n\n' + r'Air demand discharging ($\frac{\mathrm{m}^3_'
                 r'{\mathrm{n}}}{\mathrm{min}}$)')

    ax.zaxis.set_rotate_label(False)  # disable automatic rotation
    ax.set_zlabel(r'Round-trip efficiency (%)', rotation=90)

    ax.view_init(elev=15, azim=30)

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    base_style = PLTbase()
    plot_3d()
