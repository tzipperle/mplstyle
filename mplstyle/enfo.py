import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler
from .base import PLTbase


class PLTenfo(PLTbase):
    """ PLTenfo class, child of PLTbase"""

    _ENFO = 'enfo'

    def __init__(self):
        PLTbase.__init__(self)

        available_styles = {
            'color_style': [self._ENFO],
            'plt_style': [self._ENFO]}

        self._add_available_styles(available_styles)

    def _get_colors(self, style):
        if style == self._ENFO:
            return {
                'Steinkohle': (88, 88, 90),
                'Braunkohle': (116, 66, 65),
                'Mineralölprodukte': (120, 81, 80),
                'Mineralöle': (120, 81, 80),
                'Öl': (120, 81, 80),
                'Gas': (255, 230, 72),
                'Erdgas': (255, 230, 72),
                'Nichterneuerbare Abfälle': (105, 8, 90),
                'Strom': (147, 78, 136),
                'Fernwärme': (214, 76, 19),
                'Erneuerbare Energien': (0, 124, 48),
                'Beleuchtung': (255, 230, 72),
                'Mechanische Energie': (0, 0, 128),
                'IKT': (96, 101, 250),
                'Prozesswärme': (156, 13, 22),
                'Warmwasser': (255, 102, 0),
                'Raumwärme': (220, 154, 79),
                'Prozesskälte': (51, 102, 255),
                'Klimakälte': (0, 153, 204),
                'Kühlen/Lüften/Haustechnik': (147, 127, 96),
                'Sonstige': (217, 218, 219),
                'Wasserstoff': (204, 210, 116),
                'Personenverkehr': (0, 115, 207),
                'Güterverkehr': (152, 198, 234),
                'Kernenergie': (196, 7, 27),
                'Nettoimporte Strom': (217, 218, 219),
                'Sonstige Sekundärenergieträger': (148, 182, 210),
            }
        return None

    def _set_plt_style(self, style, colors, prop_cycle_colors):
        if style == self._ENFO:
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
