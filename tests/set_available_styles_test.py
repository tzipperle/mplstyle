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
def test_available_styles(used_class):
    available_styles = used_class._styles_available

    # test plt_style
    if 'plt_style' in available_styles:
        for style in available_styles['plt_style']:
            used_class.set_style(plt_style=style)

    # test color_style
    if 'color_style' in available_styles:
        for style in available_styles['color_style']:
            used_class.set_style(color_style=style)

    # test color_order_style
    if 'color_order_style' in available_styles:
        for style in available_styles['color_order_style']:
            used_class.set_style(color_order_style=style, color_style=style)
