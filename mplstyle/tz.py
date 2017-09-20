import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler
from .base import PLTbase


class PLTtz(PLTbase):
    """ PLTtz class, child of PLTbase"""

    _BLUE = 'blue'
    _JUPYTER_NOTEBOOK = 'jupyter-notebook'
    _MPL_V2 = 'mpl2_colors'

    def __init__(self):
        PLTbase.__init__(self)

        available_styles = {
            'color_style': [self._BLUE, self._MPL_V2],
            'color_order_style': [self._BLUE, self._MPL_V2],
            'plt_style': [self._JUPYTER_NOTEBOOK]}

        self._add_available_styles(available_styles)

    def _get_colors(self, style):
        if style == self._BLUE:
            return {
                'darkblue': (11, 85, 159),
                'mdarkblue': (42, 122, 185),
                'mediumblue': (83, 157, 204),
                'mlightblue': (136, 190, 220),
                'lightblue': (186, 214, 234),
                'pastelblue': (218, 232, 245),
            }
        if style == self._MPL_V2:
            return {
                'c0': '#1f77b4',
                'c1': '#ff7f0e',
                'c2': '#2ca02c',
                'c3': '#d62728',
                'c4': '#9467bd',
                'c5': '#8c564b',
                'c6': '#e377c2',
                'c7': '#7f7f7f',
                'c8': '#bcbd22',
                'c9': '#17becf'
            }
        return None

    def _get_colors_order(self, style):
        if style == self._BLUE:
            return ['darkblue', 'mdarkblue', 'mediumblue', 'mlightblue',
                    'lightblue', 'pastelblue']
        elif style == self._MPL_V2:
            return ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
        return None

    def _set_plt_style(self, style, colors, prop_cycle_colors):
        if style == self._JUPYTER_NOTEBOOK:
            plt.style.use('default')
            fntsz = 12
            lw = 2
            fntcol = 'black'
            font = {'family': 'arial', 'weight': 'normal', 'size': fntsz}
            mpl.rc('font', **font)
            mpl.rc('figure', titlesize=fntsz)
            mpl.rc('legend', framealpha=None, edgecolor='gainsboro',
                   fontsize=fntsz - 2, numpoints=1, handlelength=1,
                   loc='best', frameon=True, shadow=False, fancybox=False)
            mpl.rc('text', color=fntcol)
            mpl.rc('axes', edgecolor=fntcol, grid=True, xmargin=0,
                   labelsize=fntsz - 1, titlesize=fntsz, linewidth=0.9,
                   prop_cycle=cycler('color', prop_cycle_colors))
            mpl.rc('axes.spines', right=False, top=False)
            mpl.rc('grid', linestyle='-', color='darkgrey', linewidth=0.5,
                   alpha=0.35)
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', color=fntcol, labelsize=fntsz - 2)
            mpl.rc('ytick', color=fntcol, labelsize=fntsz - 2)

            return True
        return False
