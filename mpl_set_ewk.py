from mpl_set_base import PlotBase
import matplotlib as mpl
from cycler import cycler


class EWKPlot(PlotBase):
    def _get_colors(self, style):
        if style == 'example':
            return {
                'mdarkred': (187 / 255, 63 / 255, 63 / 255),
                'mediumred': (244 / 255, 54 / 255, 5 / 255),
                'mlightred': (250 / 255, 128 / 255, 114 / 255),
                'lightred': (255 / 255, 177 / 255, 154 / 255),
                'darkgreen': (10 / 255, 72 / 255, 30 / 255),
                'mdarkgreen': (79 / 255, 145 / 255, 83 / 255),
                'mediumgreen': (82 / 255, 171 / 255, 82 / 255),
                'mlightgreen': (131 / 255, 191 / 255, 150 / 255),
                'lightgreen': (178 / 255, 213 / 255, 189 / 255),
                'darkblue': (1 / 255, 21 / 255, 62 / 255),
                'mdarkblue': (0 / 255, 82 / 255, 147 / 255),
                'mediumblue': (100 / 255, 149 / 255, 237 / 255),
                'mlightblue': (177 / 255, 202 / 255, 246 / 255),
                'lightblue': (208 / 255, 227 / 255, 253 / 255),
                'darkred': (157 / 255, 2 / 255, 22 / 255),
                'black': (0, 0, 0),
                'darkgrey': (76 / 255, 76 / 255, 76 / 255),
                'mediumgrey': (127 / 255, 127 / 255, 127 / 255),
                'mlightgrey': (178 / 255, 178 / 255, 178 / 255),
                'lightgrey': (216 / 255, 216 / 255, 216 / 255),
            }
        return None

    def _get_colors_order(self, style):
        if style == 'example':
            return ['darkblue', 'mdarkblue', 'mediumblue',
                    'mlightblue', 'lightblue', 'darkred', 'mdarkred',
                    'mediumred', 'mlightred', 'lightred', 'darkgreen',
                    'mdarkgreen', 'mediumgreen', 'mlightgreen',
                    'lightgreen', 'black', 'darkgrey', 'mediumgrey',
                    'mlightgrey', 'lightgrey']
        return None

    def _set_plt_style(self, style, colors, prop_cycle_colors):
        if style == 'example':
            fs = 18
            lw = 2
            mpl.rc('font', size=fs)
            mpl.rc('figure', figsize=[11, 7], titlesize=fs)
            mpl.rc('legend', framealpha=None,
                   edgecolor=colors['darkred'],
                   fontsize=fs - 2, numpoints=1, handlelength=1,
                   loc='best')
            mpl.rc('axes', edgecolor=colors['lightgrey'], grid=True,
                   xmargin=0, labelsize=fs, titlesize=fs)
            mpl.rc('grid', linestyle=':', color=self._colors['mlightgrey'])
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', labelsize=fs - 2)
            mpl.rc('ytick', labelsize=fs - 2)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        return False
