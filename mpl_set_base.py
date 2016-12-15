import matplotlib as mpl
from cycler import cycler


class PlotBase:
    DEFAULT_COLOR_ORDER = ['mediumblue', 'darkblue', 'mdarkblue',
                           'mlightblue', 'lightblue', 'mediumred', 'darkred',
                           'mdarkred', 'mlightred', 'lightred', 'mediumgreen',
                           'darkgreen', 'mdarkgreen', 'mlightgreen',
                           'lightgreen', 'mediumgrey', 'black', 'darkgrey',
                           'mlightgrey', 'lightgrey']

    DEFAULT_COLORS = {'darkblue': (1 / 255, 21 / 255, 62 / 255),
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

    def _set_default_plt_style(self):
        fs = 18
        lw = 2
        mpl.rc('font', size=fs)
        mpl.rc('figure', figsize=[11, 7], titlesize=fs)
        mpl.rc('legend', framealpha=None,
               edgecolor=self._colors['lightgrey'],
               fontsize=fs - 2, numpoints=1, handlelength=1,
               loc='upper right')
        mpl.rc('axes', edgecolor=self._colors['lightgrey'], grid=True,
               xmargin=0, labelsize=fs, titlesize=fs)
        mpl.rc('grid', linestyle=':', color=self._colors['mlightgrey'])
        mpl.rc('lines', lw=lw, markersize=10)
        mpl.rc('xtick', labelsize=fs - 2)
        mpl.rc('ytick', labelsize=fs - 2)
        mpl.rcParams['axes.prop_cycle'] = cycler('color',
                                                 self._prop_cycle_colors)

    def __init__(self, plt_style='default', color_style='default',
                 color_order_style='default'):
        self._color_style = color_style
        self._color_order_style = color_order_style
        self._plt_style = plt_style
        self._colors_order = None
        self._colors = None
        self.set_style()

    def set_all_style(self, style):
        self._color_order_style = style
        self._color_style = style
        self._plt_style = style

    def set_style(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        self._set_colors()
        self._set_color_order()

        self._check_color_consistence()

        self.__sort_colors_cycle()
        self._set_selected_plt_style()

    def _set_color_order(self):
        if self._color_order_style == 'default':
            self._colors_order = self.DEFAULT_COLOR_ORDER
        else:
            self._colors_order = self._get_colors_order(
                self._color_order_style)
        if self._colors_order is None:
            raise NotImplementedError(
                'Color order style {} not defined'.format(
                    self._color_order_style))

    def _set_selected_plt_style(self):
        if self._plt_style == 'default':
            self._set_default_plt_style()
        else:
            success = self._set_plt_style(self._plt_style, self._colors,
                                          self._prop_cycle_colors)
            if not success:
                raise NotImplementedError(
                    'Plt style {} not defined'.format(self._plt_style))

    def _set_colors(self):
        if self._color_style == 'default':
            self._colors = self.DEFAULT_COLORS
        else:
            self._colors = self._get_colors(self._color_style)
        if self._colors is None:
            raise NotImplementedError(
                'Color style {} not defined'.format(self._color_style))

    def _check_color_consistence(self):
        colors = self._colors
        sort_order = self._colors_order
        for c in sort_order:
            if not c in colors:
                raise AttributeError(
                    'The color \'{}\' in the sort order style \'{}\''
                    ' is not defined in the colors style \'{}\''.format(
                        c, self._color_order_style, self._color_style))

    def get_colors(self):
        return self._colors

    def get_order(self):
        return self._colors_order

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
        colors = self._colors
        sort_order = self._colors_order

        color_list = []
        for i, l in enumerate(sort_order):
            color_list.append(colors[l])

        self._prop_cycle_colors = color_list

    def _get_colors(self, style):
        return self.DEFAULT_COLORS

    def _get_colors_order(self, style):
        return self.DEFAULT_COLOR_ORDER

    def _set_plt_style(self, style, colors, prop_cycle_colors):
        self._set_default_plt_style()
