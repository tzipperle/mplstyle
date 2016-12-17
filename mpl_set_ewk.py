from mpl_set_base import PlotBase
import matplotlib as mpl
from cycler import cycler


class EWKPlot(PlotBase):
    """ EWKPlot class, children of PlotBase"""

    def _get_colors(self, style):
        if style == 'example':
            return {
                'mdarkred': (187, 63, 63),
                'mediumred': (244, 54, 5),
                'lightred': (255, 177, 154),
                'darkgreen': (10, 72, 30),
                'mediumgreen': (82, 171, 82),
                'mlightgreen': (131, 191, 150),
                'lightgreen': (178, 213, 189),
                'darkblue': (1, 21, 62),
                'mediumblue': (100, 149, 237),
                'lightblue': (208, 227, 253),
                'darkred': (157, 2, 22),
                'black': (0, 0, 0),
                'darkgrey': (76, 76, 76),
                'mediumgrey': (127, 127, 127),
                'mlightgrey': (178, 178, 178),
            }
        return None

    def _get_colors_order(self, style):
        if style == 'example':
            return ['mdarkred', 'mediumred', 'lightred', 'darkgreen',
                    'mediumgreen', 'mlightgreen', 'lightgreen', 'darkblue',
                    'mediumblue', 'lightblue', 'darkred', 'black', 'darkgrey',
                    'mediumgrey', 'mlightgrey', ]
        return None

    def _set_plt_style(self, style, colors, prop_cycle_colors):
        if style == 'example':
            mpl.style.use('ggplot')
            figsz = 12
            fntsz = 18
            lw = 2
            fntcol = 'dimgray'  # self._colors['darkgrey']

            font = {'family': 'arial', 'weight': 'light', 'size': fntsz}
            mpl.rc('font', **font)
            mpl.rc('figure', figsize=(figsz, figsz / 1.8), titlesize=fntsz)
            mpl.rc('legend', framealpha=None, fancybox=True,
                   edgecolor=colors['mlightgrey'], fontsize=fntsz - 2,
                   numpoints=1, handlelength=1,
                   loc='best')
            mpl.rcParams['text.color'] = fntcol
            mpl.rc('axes', edgecolor='w', grid=True,
                   xmargin=0, labelsize=fntsz-2, titlesize=fntsz)
            mpl.rc('grid', color='w', linestyle='-', linewidth=0.5)
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', color=fntcol, labelsize=fntsz - 2)
            mpl.rc('ytick', color=fntcol, labelsize=fntsz - 2)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        return False
