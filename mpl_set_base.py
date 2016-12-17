import matplotlib as mpl
from cycler import cycler


class PlotBase:
    """ Set own plot and color style."""

    _DEFAULT_COLOR_ORDER = ['mediumblue', 'darkblue', 'mdarkblue', 'mlightblue',
                           'lightblue', 'mediumred', 'darkred',
                           'mdarkred', 'mlightred', 'lightred', 'mediumgreen',
                           'darkgreen', 'mdarkgreen', 'mlightgreen',
                           'lightgreen', 'mediumgrey', 'black', 'darkgrey',
                           'mlightgrey', 'lightgrey']

    _DEFAULT_COLORS = {  # (R,G,B) tuples with range (0-255)
        'darkblue': (1, 21, 62),
        'mdarkblue': (0, 82, 147),
        'mediumblue': (100, 149, 237),
        'mlightblue': (177, 202, 246),
        'lightblue': (208, 227, 253),
        'darkred': (157, 2, 22),
        'mdarkred': (187, 63, 63),
        'mediumred': (244, 54, 5),
        'mlightred': (250, 128, 114),
        'lightred': (255, 177, 154),
        'darkgreen': (10, 72, 30),
        'mdarkgreen': (79, 145, 83),
        'mediumgreen': (82, 171, 82),
        'mlightgreen': (131, 191, 150),
        'lightgreen': (178, 213, 189),
        'black': (0, 0, 0),
        'darkgrey': (76, 76, 76),
        'mediumgrey': (127, 127, 127),
        'mlightgrey': (178, 178, 178),
        'lightgrey': (216, 216, 216),
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
        """ Set plot style, colors and color order.

        Args:
            plt_style: optional string for plt style; default: ('default')
            color_style: optional string for color order; default: ('default')
            color_order_style: optional string for color order style;
                                default: ('default')
        """
        self._color_style = color_style
        self._color_order_style = color_order_style
        self._plt_style = plt_style
        self._colors_order = None
        self._colors = None
        self.set_style()

    def set_all_style(self, style='default'):
        """ Set same style for all options.

        Args:
            style: string for chosen style; default: ('default')
        """
        self._color_style = style
        self._color_order_style = style
        self._plt_style = style
        self.set_style()

    def set_style(self, **kwargs):
        """ Set plot style, colors and color order.

        Args:
            plt_style: optional string for plt style; default: ('default')
            color_style: optional string for color order; default: ('default')
            color_order_style: optional string for color order style;
                                default: ('default')
        """
        for k, v in kwargs.items():
            setattr(self, k, v)

        self._set_colors()
        self._set_color_order()

        self._check_color_consistence()

        self.__sort_colors_cycle()
        self._set_selected_plt_style()

    def _set_color_order(self):
        if self._color_order_style == 'default':
            self._colors_order = self._DEFAULT_COLOR_ORDER
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
            _colors = self._DEFAULT_COLORS.copy()
        else:
            _colors = self._get_colors(self._color_style).copy()
        if _colors is None:
            raise NotImplementedError(
                'Color style {} not defined'.format(self._color_style))

        self._colors = self._to_rgb_mpl(_colors)

    def _to_rgb_mpl(self, _colors):
        _to_rgb = lambda r, g, b: tuple(x / 255. for x in (r, g, b))
        for key, val in _colors.items():
            _colors[key] = _to_rgb(*val)
        return _colors

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
        """ Get colors form chosen style.

        Returns:
            Dictionary of colors
        """
        return self._colors

    def get_color_order(self):
        """ Get ordered color list form chosen style.

        Returns:
            List of ordered colors
        """
        return self._colors_order

    def add_zbild(self, ax, xloc, yloc, zbild, tum=True, fontsize=10,
                  color='grey'):
        """ Set ZBild number as text in the chart.

        Args:
            ax: a matplotlib Axes instance
            xloc: float for position; ymin = 0, ymax = 1
            yloc: float for position; xmin = 0, xmax = 1
            zbild: string for text
            tum: optional boolean; for copyright; default: (tum=True)
            fontsize: optional float for font size; default: (10)
            color: optional string for mpl color; default: ('gray')
        """
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
        return self._DEFAULT_COLORS

    def _get_colors_order(self, style):
        return self._DEFAULT_COLOR_ORDER

    def _set_plt_style(self, style, colors, prop_cycle_colors):
        self._set_default_plt_style()
