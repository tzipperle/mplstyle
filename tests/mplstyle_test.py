import pytest
import matplotlib as mpl
from cycler import cycler
from mplstyle.base import PLTbase


class TestModel:
    @pytest.fixture(scope='module')
    def base_style(self):
        return PLTbase()

    def get_default_color_order(self, base_style):
        return [(r / 255., g / 255., b / 255.) for r, g, b in
                base_style._DEFAULT_COLORS.values()]

    def get_default_colors(self, base_style):
        return {key: (val[0] / 255., val[1] / 255., val[2] / 255.)
                for key, val in base_style._DEFAULT_COLORS.items()}

    def test_set_style(self, base_style):
        # test mplstyle.set_style('default')
        mpl.rcdefaults()
        init_rc = mpl.rcParams.copy()

        base_style._set_default_plt_style()
        traget_base = mpl.rcParams.copy()

        mpl.rcdefaults()
        default_rc = mpl.rcParams.copy()

        base_style.set_style('default')
        mplstyle_base_rc = mpl.rcParams.copy()

        assert init_rc == default_rc
        assert init_rc != traget_base
        assert traget_base == mplstyle_base_rc

    def test_color_order_style(self, base_style):
        # test mplstyle.set_style(color_order_style='default') and
        # mplstyle.get_color_order()
        default_color_order = cycler('color',
                                     self.get_default_color_order(base_style))
        base_style.set_style(color_order_style='default')

        assert default_color_order == mpl.rcParams['axes.prop_cycle']
        assert base_style._DEFAULT_COLOR_ORDER == base_style.get_color_order()

    def test_color_style(self, base_style):
        # test mplstyle.set_style(color_style='default') and
        # mplstyle.get_colors()
        base_colors = self.get_default_colors(base_style)
        base_style.set_style(color_style='default')

        get_base_colors = base_style.get_colors()

        assert base_colors == get_base_colors
