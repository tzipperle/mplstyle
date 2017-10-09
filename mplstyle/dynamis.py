import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler
from .base import PLTbase


class PLTdynamis(PLTbase):
    """ PLTdynamis class, child of PLTbase"""

    _DYN = 'dyn'
    _DYN_KLEE = 'dyn_klee'

    def __init__(self):
        PLTbase.__init__(self)

        available_styles = {
            'color_style': [self._DYN, self._DYN_KLEE],
            'plt_style': [self._DYN]}

        self._add_available_styles(available_styles)

    def _get_colors(self, style):
        if style == self._DYN:
            return {
                'rw': (153, 0, 0),
                'ww': (191, 0, 0),
                'pw': (255, 102, 102),
                'spw': (255, 229, 204),
                'pk': (24, 116, 205),
                'kk': (0, 0, 128),
                'me': (224, 224, 224),
                'b': (240, 240, 111),
                'ikt': (154, 205, 50),
            }
        elif style == self._DYN_KLEE:
            return {
                'rw': (255, 153, 0),
                'ww': (255, 102, 0),
                'pw': (255, 0, 0),
                'spw': (255, 0, 0),
                'pk': (51, 102, 255),
                'kk': (1, 153, 204),
                'me': (0, 0, 128),
                'b': (255, 255, 153),
                'ikt': (255, 0, 255),
            }
        return None

    def _set_plt_style(self, style, colors, prop_cycle_colors):
        if style == self._DYN:
            plt.style.use('default')
            fntsz = 18
            lw = 2
            fntcol = 'black'
            font = {'family': 'arial', 'weight': 'normal', 'size': fntsz}
            mpl.rc('font', **font)
            mpl.rc('figure', figsize=[11, 7], titlesize=fntsz)
            mpl.rc('legend', framealpha=None,
                   edgecolor='gainsboro',
                   fontsize=fntsz - 2, numpoints=1, handlelength=1,
                   loc='best', frameon=True, shadow=False,
                   fancybox=False)
            mpl.rcParams['text.color'] = fntcol
            mpl.rc('axes', edgecolor=fntcol, grid=True,
                   xmargin=0, labelsize=fntsz - 1, titlesize=fntsz,
                   linewidth=0.9)
            mpl.rcParams['axes.spines.right'] = False
            mpl.rcParams['axes.spines.top'] = False
            mpl.rc('grid', linestyle=':', color='darkgrey',
                   linewidth=0.5)
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', color=fntcol, labelsize=fntsz - 2)
            mpl.rc('ytick', color=fntcol, labelsize=fntsz - 2)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        return False
