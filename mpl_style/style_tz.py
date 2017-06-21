# -*- coding: utf-8 -*-
from .style_base import PLTbase
import matplotlib as mpl
from cycler import cycler


class PLTtz(PLTbase):
    """ PLTtz class, child of PLTbase"""

    BLUE = 'blue'
    JUPYTER_NOTEBOOK = 'jupyter-notebook'

    def __init__(self):
        PLTbase.__init__(self)

        styles_available = {
            'color_style': [self.BLUE],
            'color_order_style': [self.BLUE],
            'plt_style': [self.JUPYTER_NOTEBOOK]}

        self._add_available_styles(styles_available)
    def _get_colors(self, style):
        if style == self.BLUE:
            return {
                'darkblue': (11, 85, 159),
                'mdarkblue': (42, 122, 185),
                'mediumblue': (83, 157, 204),
                'mlightblue': (136, 190, 220),
                'lightblue': (186, 214, 234),
                'pastelblue': (218, 232, 245),
            }
        return None

    def _get_colors_order(self, style):
        if style == self.BLUE:
            return ['darkblue', 'mdarkblue', 'mediumblue', 'mlightblue',
                    'lightblue', 'pastelblue']
        return None

    def _set_plt_style(self, style, colors, prop_cycle_colors):
        if style == self.JUPYTER_NOTEBOOK:
            mpl.style.use('default')
            fntsz = 12
            lw = 2
            fntcol = 'black'
            font = {'family': 'arial', 'weight': 'normal', 'size': fntsz}
            mpl.rc('font', **font)
            mpl.rc('figure', titlesize=fntsz)
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
            mpl.rc('grid', linestyle='-', color='darkgrey',
                   linewidth=0.5, alpha=0.35)
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', color=fntcol, labelsize=fntsz - 2)
            mpl.rc('ytick', color=fntcol, labelsize=fntsz - 2)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     prop_cycle_colors)
            return True
        return False
