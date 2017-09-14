import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from mplstyle.ewk import PLTewk


def read_data(name):
    df = pd.read_excel(name).set_index('jahr')
    return df


def plot_fig(df, title):
    colors = ewk_plt.get_colors()

    gs = mpl.gridspec.GridSpec(2, 1, height_ratios=[1, 0.1])
    fig = plt.figure(figsize=[11, 8])
    ax = fig.add_subplot(gs[0])

    color = [colors[i] for i in df.columns]
    df.plot.bar(ax=ax, stacked=True, width=0.5, edgecolor=None,
                zorder=2, rot=0, legend=False, color=color)

    ax.set_xlabel('').set_visible(False)

    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc='upper center', ncol=3,
              bbox_to_anchor=(0.5, -0.04))

    ax.set_title(title, fontsize=20, fontweight='bold')
    fig.tight_layout()
    plt.show()


def _x_axis_tick(ax, n=5):
    ticks = ax.xaxis.get_ticklocs()
    ticklabels = [l.get_text() for l in ax.xaxis.get_ticklabels()]
    ax.xaxis.set_ticks(ticks[::n])
    ax.xaxis.set_ticklabels(ticklabels[::n])
    return ax


if __name__ == '__main__':
    ewk_plt = PLTewk()
    ewk_plt.set_style('ewk')

    name_input_file = 'ghd_bs'
    title = 'GHD Endenergieverbrauch in PJ nach Brennstoffen'

    data = read_data('{}.xlsx'.format(name_input_file))
    plot_fig(data, title=title)
