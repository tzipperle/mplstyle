.. currentmodule:: mpl-style

.. _api:

API
========================
List of commands, which can be applied on initialized instance of the chosen class, is presented in the following. 

.. function:: set_style(a, b)

  Chooses style for **color**, **color order** and **plt style**.   
  
  :param a: first input;
  :param b: second input.

.. function:: get_colors()

  :return: dictionary of colors used in the chosen **color style**.  

.. function:: get_color_order()

  :return: list of colors from the chosen **color order style** in order of appearance.
  
.. function:: get_available_styles()

  :return: all available styles for each plotting setting (**color**, **color order** and **plt style**).
  
.. function:: get_selected_style()

  :return: chosen style for **color**, **color order** and **plt style**.
  
.. function:: get_cmap(colors, position=None, bit=False)

  Generates custom color maps for Matplotlib. The method allows to create a list of tuples with 8-bit (0 to 255)
  or arithmetic (0.0 to 1.0) RGB values for making linear color maps. Color tuple placed first characterizes the 
  lowest value of the color bar. The last tuple represents the the highest value.   
  
  :param colors: list of RGB tuples with 8-bit (0 to 255) or arithmetic (0 to 1), default: arithmetic;
  :param position: list from 0 to 1, which dictates the location for each color; 
  :param bit: boolean, default: False (arithmetic), True (RGB);
  
  :return: **cmap** - a color map with equally spaced colors.
  
  :Example: cmap = mpl-style.get_cmap(colors=[(255, 0, 0), (0, 157, 0)], bit=True)
            cmap = mpl-style.get_cmap([(1, 1, 1), (0.5, 0, 0)], position=[0, 1]))


  

