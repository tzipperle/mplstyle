import pandas as pd
import matplotlib.pyplot as plt
from mplstyle.ewk import PLTewk


def read_data(name):
    df = pd.read_excel(name).set_index('jahr')
    return df


def plot_fig(df, title):
    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=[11, 8],
                                   gridspec_kw={'height_ratios': [1, 0.1]})
    ax1.axis('off')

    colors = ewk_plt.get_colors()
    color = [colors[i] for i in df.columns]
    df.plot.bar(ax=ax0, stacked=True, width=0.5, edgecolor=None,
                zorder=2, rot=0, legend=False, color=color)

    handles, labels = ax0.get_legend_handles_labels()
    ax0.legend(handles, labels, loc='upper center', ncol=3,
               bbox_to_anchor=(0.5, -0.04))

    ax0.set_title(title, fontsize=20, fontweight='bold')
    ax0.set_xlabel('').set_visible(False)
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    ewk_plt = PLTewk()
    ewk_plt.set_style('ewk')

    data = read_data('ghd_bs.xlsx')

    plot_fig(data, title='GHD Endenergieverbrauch in PJ nach Brennstoffen')
