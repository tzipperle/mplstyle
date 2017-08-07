import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler
from .base import PLTbase


class PLTdatabay(PLTbase):
    """ PLTdatabay class, children of PLTbase"""

    _DATAYBAY = 'databay'
    _DATAYBAY2 = 'databay2'
    _TEST = 'test'

    def __init__(self):
        PLTbase.__init__(self)

        available_styles = {
            'color_style': [self._DATAYBAY, self._DATAYBAY2],
            'color_order_style': [self._DATAYBAY],
            'plt_style': [self._DATAYBAY, self._TEST]}

        self._add_available_styles(available_styles)

    def _get_colors(self, style):
        if style == self._DATAYBAY:
            return {
                'darkblue': (9, 30, 67),
                'mdarkblue': (21, 71, 157),
                'mediumblue': (53, 117, 227),
                'mlightblue': (143, 178, 240),
                'lightblue': (210, 224, 249),
                'darkred': (65, 12, 12),
                'mdarkred': (151, 28, 28),
                'mediumred': (219, 61, 61),
                'mlightred': (235, 147, 147),
                'lightred': (247, 212, 212),
                'darkgreen': (26, 51, 26),
                'mdarkgreen': (61, 118, 61),
                'mediumgreen': (83, 172, 83),
                'mlightgreen': (152, 205, 152),
                'lightgreen': (204, 229, 204),
                'black': (0, 0, 0),
                'darkgrey': (76, 76, 76),
                'mediumgrey': (127, 127, 127),
                'mlightgrey': (178, 178, 178),
                'lightgrey': (216, 216, 216),
            }
        elif style == self._DATAYBAY2:
            return {
                'darkblue': (21, 41, 55),
                'mdarkblue': (49, 95, 129),
                'mediumblue': (89, 147, 192),
                'mlightblue': (163, 195, 220),
                'lightblue': (218, 231, 241),
                'darkred': (78, 24, 24),
                'mdarkred': (137, 42, 42),
                'mediumred': (201, 79, 79),
                'mlightred': (225, 157, 157),
                'lightred': (243, 216, 216),
                'darkgreen': (21, 55, 36),
                'mdarkgreen': (49, 129, 83),
                'mediumgreen': (89, 192, 132),
                'mlightgreen': (163, 220, 187),
                'lightgreen': (218, 241, 228),
                'black': (0, 0, 0),
                'darkgrey': (76, 76, 76),
                'mediumgrey': (127, 127, 127),
                'mlightgrey': (178, 178, 178),
                'lightgrey': (216, 216, 216),
            }
        return None

    def _get_colors_order(self, style):
        if style == self._DATAYBAY:
            return ['darkblue', 'mdarkblue', 'mediumblue', 'mlightblue',
                    'lightblue',
                    'darkred', 'mdarkred', 'mediumred', 'mlightred',
                    'lightred',
                    'darkgreen', 'mdarkgreen', 'mediumgreen', 'mlightgreen',
                    'lightgreen',
                    'black', 'darkgrey', 'mediumgrey', 'mlightgrey',
                    'lightgrey']
        return None

    def _set_plt_style(self, style, colors, prop_cycle_colors):
        if style == self._DATAYBAY:
            plt.style.use('default')
            fs = 18
            lw = 2
            fntcol = 'black'

            font = {'family': 'arial', 'weight': 'normal', 'size': fs}
            mpl.rc('font', **font)
            mpl.rc('figure', figsize=[11, 7], titlesize=fs)
            mpl.rc('legend', framealpha=None,
                   edgecolor=colors['mlightgrey'],
                   fontsize=fs - 2, numpoints=1, handlelength=1,
                   loc='best', frameon=True, shadow=False,
                   fancybox=False)
            mpl.rcParams['text.color'] = colors[fntcol]
            mpl.rc('axes', edgecolor=colors['black'], grid=True,
                   xmargin=0, labelsize=fs, titlesize=fs, linewidth=0.8)
            mpl.rcParams['axes.spines.right'] = False
            mpl.rcParams['axes.spines.top'] = False
            mpl.rc('grid', linestyle=':', color=colors['mediumgrey'],
                   linewidth=0.5)
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', color=colors[fntcol], labelsize=fs - 2)
            mpl.rc('ytick', color=colors[fntcol], labelsize=fs - 2)

            return True
        elif style == self._TEST:
            plt.style.use('default')
            fs = 18
            lw = 2
            fntcol = 'black'

            font = {'family': 'arial', 'weight': 'normal', 'size': fs}
            mpl.rc('font', **font)
            mpl.rc('figure', figsize=[11, 7], titlesize=fs)
            mpl.rc('legend', framealpha=None,
                   edgecolor=colors['lightgrey'],
                   fontsize=fs - 2, numpoints=1, handlelength=1,
                   loc='best', frameon=True, shadow=False)
            mpl.rcParams['text.color'] = colors[fntcol]
            mpl.rc('axes', edgecolor=colors['black'], grid=True,
                   xmargin=0, labelsize=fs, titlesize=fs, linewidth=1)
            mpl.rcParams['axes.spines.right'] = False
            mpl.rcParams['axes.spines.top'] = False
            mpl.rc('grid',
                   linestyle=':', color=colors['mlightgrey'], linewidth=0.5)
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', color=colors[fntcol], labelsize=fs - 2)
            mpl.rc('ytick', color=colors[fntcol], labelsize=fs - 2)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        return False
