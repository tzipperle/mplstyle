import matplotlib as mpl
from cycler import cycler
from .base import PLTbase


class PLTewk(PLTbase):
    """ PLTewk class, child of PLTbase"""

    _EXAMPLE = 'example'
    _EKW = 'ewk'

    def __init__(self):
        PLTbase.__init__(self)

        available_styles = {
            'color_style': [self._EXAMPLE, self._EKW],
            'color_order_style': [self._EXAMPLE],
            'plt_style': [self._EXAMPLE, self._EKW]}

        self._add_available_styles(available_styles)

    def _get_colors(self, style):

        if style is self._EXAMPLE:
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
        elif style is self._EKW:
            return {
                'Steinkohle': (88, 88, 90),
                'Braunkohle': (116, 66, 65),
                'Öl': (120, 81, 80),
                'Gas': (255, 230, 72),
                'Strom': (147, 78, 136),
                'Fernwärme': (214, 76, 19),
                'Erneuerbare Energien': (0, 124, 48),
                'Kernenergie': (196, 7, 27),
            }
        return None

    def _get_colors_order(self, style):

        if style is self._EXAMPLE:
            return ['mdarkred', 'mediumred', 'lightred', 'darkgreen',
                    'mediumgreen', 'mlightgreen', 'lightgreen', 'darkblue',
                    'mediumblue', 'lightblue', 'darkred', 'black', 'darkgrey',
                    'mediumgrey', 'mlightgrey']
        return None

    def _set_plt_style(self, style, colors, prop_cycle_colors):

        if style is self._EXAMPLE:
            mpl.style.use('ggplot')
            figsz = 12
            fntsz = 18
            lw = 2
            fntcol = 'dimgray'
            font = {'family': 'arial', 'weight': 'light', 'size': fntsz}
            mpl.rc('font', **font)
            mpl.rc('figure', figsize=(figsz, figsz / 1.8), titlesize=fntsz)
            mpl.rc('legend', framealpha=None, fancybox=True,
                   edgecolor=colors['mlightgrey'], fontsize=fntsz - 2,
                   numpoints=1, handlelength=1,
                   loc='best')
            mpl.rcParams['text.color'] = fntcol
            mpl.rc('axes', edgecolor='w', grid=True,
                   xmargin=0, labelsize=fntsz - 2, titlesize=fntsz)
            mpl.rc('grid', color='w', linestyle='-', linewidth=0.5)
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', color=fntcol, labelsize=fntsz - 2)
            mpl.rc('ytick', color=fntcol, labelsize=fntsz - 2)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        elif style is self._EKW:
            mpl.style.use('default')
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
            # add default colors to first postion (default color order)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        return False
