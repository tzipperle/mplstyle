import pytest
from mplstyle.base import PLTbase
from mplstyle.databay import PLTdatabay
from mplstyle.dynamis import PLTdynamis
from mplstyle.enfo import PLTenfo
from mplstyle.ewk import PLTewk
from mplstyle.tz import PLTtz


@pytest.mark.parametrize('used_class',
                         [PLTtz(), PLTewk(), PLTenfo(), PLTdynamis(),
                          PLTdatabay(), PLTbase()])
class TestModel(object):
    def test_two_args(self, used_class):
        with pytest.raises(ValueError):
            used_class.set_style('no-style', 'no-style2')

    def test_wrong_arg(self, used_class):
        with pytest.raises(NotImplementedError):
            used_class.set_style(wrong_arg='default')

    def test_plt_style(self, used_class):
        with pytest.raises(NotImplementedError):
            used_class.set_style(plt_style='no-style')

    def test_color_style(self, used_class):
        with pytest.raises(NotImplementedError):
            used_class.set_style(color_style='no-style')

    def test_color_order_style(self, used_class):
        with pytest.raises(NotImplementedError):
            used_class.set_style(color_order_style='no-style',
                                 color_style='default')

        with pytest.raises(NotImplementedError):
            used_class.set_style(color_order_style='no-style')
