import matplotlib as mpl
from cycler import cycler
from abc import ABCMeta, abstractmethod


class PlotBase(metaclass=ABCMeta):
    def __init__(self, plt_style='default', color_style='default',
                 color_order_style='default'):
        self.color_style = color_style
        self.color_order_style = color_order_style
        self.plt_style = plt_style

    def set_style(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        # set plot style
        self._set_colors()
        self._set_colors_order()
        self.__sort_colors_cycle()
        self._set_plt_style()

    def get_colors(self):
        return self.colors

    def get_order(self):
        return self.colors_order

    def add_zbild(self, ax, xloc, yloc, zbild, tum=True, fontsize=10,
                  color='grey'):
        x_min = ax.get_xlim()[0]
        x_max = ax.get_xlim()[1]
        y_min = ax.get_ylim()[0]
        y_max = ax.get_ylim()[1]

        x = x_min + xloc * (x_max - x_min)
        y = y_min + yloc * (y_max - y_min)

        if tum == True:
            zbild = '$\copyright$ TUM IfE {}'.format(zbild)

        ax.text(x, y, zbild, fontsize=fontsize, color=color)

    def __sort_colors_cycle(self):
        colors = self.colors
        sort_order = self.colors_order

        color_list = []
        for i, l in enumerate(sort_order):
            color_list.append(colors[l])

        self._prop_cycle_colors = color_list

    @abstractmethod
    def _set_colors(self):
        pass

    @abstractmethod
    def _set_colors_order(self):
        pass

    @abstractmethod
    def _set_plt_style(self):
        pass


class EWKPlot(PlotBase):
    def _set_colors(self):
        if self.color_style == 'default':
            color_dict = {'darkblue': (1 / 255, 21 / 255, 62 / 255),
                          'mdarkblue': (0 / 255, 82 / 255, 147 / 255),
                          'mediumblue': (100 / 255, 149 / 255, 237 / 255),
                          'mlightblue': (177 / 255, 202 / 255, 246 / 255),
                          'lightblue': (208 / 255, 227 / 255, 253 / 255),
                          'darkred': (157 / 255, 2 / 255, 22 / 255),
                          'mdarkred': (187 / 255, 63 / 255, 63 / 255),
                          'mediumred': (244 / 255, 54 / 255, 5 / 255),
                          'mlightred': (250 / 255, 128 / 255, 114 / 255),
                          'lightred': (255 / 255, 177 / 255, 154 / 255),
                          'darkgreen': (10 / 255, 72 / 255, 30 / 255),
                          'mdarkgreen': (79 / 255, 145 / 255, 83 / 255),
                          'mediumgreen': (82 / 255, 171 / 255, 82 / 255),
                          'mlightgreen': (131 / 255, 191 / 255, 150 / 255),
                          'lightgreen': (178 / 255, 213 / 255, 189 / 255),
                          'black': (0, 0, 0),
                          'darkgrey': (76 / 255, 76 / 255, 76 / 255),
                          'mediumgrey': (127 / 255, 127 / 255, 127 / 255),
                          'mlightgrey': (178 / 255, 178 / 255, 178 / 255),
                          'lightgrey': (216 / 255, 216 / 255, 216 / 255),
                          }
        else:
            raise NotImplementedError(
                'Color style {} not defined'.format(self.color_style))

        self.colors = color_dict

    def _set_colors_order(self):
        if self.color_order_style == 'default':
            colors_order = ['mediumblue', 'darkblue', 'mdarkblue',
                            'mlightblue', 'lightblue', 'mediumred', 'darkred',
                            'mdarkred', 'mlightred', 'lightred', 'mediumgreen',
                            'darkgreen', 'mdarkgreen', 'mlightgreen',
                            'lightgreen', 'mediumgrey', 'black', 'darkgrey',
                            'mlightgrey', 'lightgrey']

        elif self.color_order_style == 'default-2':
            colors_order = ['darkblue', 'mdarkblue', 'mediumblue',
                            'mlightblue', 'lightblue', 'darkred', 'mdarkred',
                            'mediumred', 'mlightred', 'lightred', 'darkgreen',
                            'mdarkgreen', 'mediumgreen', 'mlightgreen',
                            'lightgreen', 'black', 'darkgrey', 'mediumgrey',
                            'mlightgrey', 'lightgrey']
        else:
            raise NotImplementedError(
                'Color order style {} not defined'.format(self.color_style))

        self.colors_order = colors_order

    def _set_plt_style(self):
        if self.plt_style == 'default':
            fs = 18
            lw = 2
            mpl.rc('font', size=fs)
            mpl.rc('figure', figsize=[11, 7], titlesize=fs)
            mpl.rc('legend', framealpha=None,
                   edgecolor=self.colors['lightgrey'],
                   fontsize=fs - 2, numpoints=1, handlelength=1,
                   loc='upper right')
            mpl.rc('axes', edgecolor=self.colors['lightgrey'], grid=True,
                   xmargin=0, labelsize=fs, titlesize=fs)
            mpl.rc('grid', linestyle=':', color=self.colors['mlightgrey'])
            mpl.rc('lines', lw=lw, markersize=10)
            mpl.rc('xtick', labelsize=fs - 2)
            mpl.rc('ytick', labelsize=fs - 2)
            mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                     self._prop_cycle_colors)

        else:
            raise NotImplementedError(
                'Plot style {} not defined'.format(self.plt_style))
