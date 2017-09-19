import pytest
import matplotlib as mpl
from cycler import cycler
from mplstyle.base import PLTbase


@pytest.fixture
def base_style():
    return PLTbase()


def test_color_odrder(base_style):
    # test default color order
    color_order = [(r / 255., g / 255., b / 255.) for r, g, b in
                   base_style._DEFAULT_COLORS.values()]

    base_style.set_style('default')

    assert cycler('color', color_order) == mpl.rcParams['axes.prop_cycle']
