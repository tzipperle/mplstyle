.. currentmodule:: mpl-style

.. _use:

How to Use
========================

This section explains and shows how any of the classes from **mpl-style** can be used. **PLTtz** class, which was already mentioned in the :ref:`overview <overview>`, is taken as an example. Its implementation in the ``trigonometric_functions.py`` is explained very detailed by moving step by step through the script. Other classes are used completely similar.

trigonometric_functions.py
"""""""""""""""""""""""
Several trigonometric functions are plotted twice in this file with two different configurations of plot settings. Both plots with chosen configuration are presented in the end. Detailed comments of the script are in the following.  

::

    import matplotlib.pyplot as plt
    import numpy as np
    import os
    import sys
    
Four packages are included: 

* `matplotlib.pyplot`_ is a plotting library which allows present results in a diagram form quite easily;
* `numpy`_ is the fundamental package for scientific computing with Python;
* `os`_ is the module for using operating system according to its functionality in a portable way;
* `sys`_ is the module, which provides access to variables and functions used by the interpreter. 

::

    sys.path.append(os.path.split(os.path.dirname(os.getcwd()))[-2])
    
This command allows to use **mpl-style** for the case, when the package wasn't added to Python search path. This step is really necessary, if, for example, you have just `downloaded`_ or cloned (with `git`_) this repository to a directory of your choice, and you want to run codes inside this directory trying to figure out how **mpl-style** is working. 

.. note::

	
        The procedure of adding **mpl-style** package to the sys.path, which will allow to include it as installed site-package, is written here. 

::

    from mpl_style.PLT_tz import PLTtz
    tz_plt=PLTtz()

Imports **PLTtz** class from a file ``PLT_tz.py``, where this class is described as a child of **PLTbase**. Then creates an instance of the class and assigns it to the local variable **tz_plt**.

.. note::

	
        When a new initialized instance of the chosen class is obtained, all three settings (**color style**, **color order style** and **plt style**) are immediately rewritten. Since this moment each setting works according to its own 'default' style, kept in **PLTbase** class. 
        
::

    fig = plt.figure(figsize=[8,6])
    ax0 = fig.add_subplot(211)

    x = np.arange(0, 2 * np.pi, 0.01)
    for c in range(4):
      y = np.sin(x) + c
      ax0.plot(x, y, label=c)

    ax0.set_title('default - default - default')
    ax0.set_ylabel(r'Pressure ($\mathrm{bar}_{\mathrm{g}}$)')
    ax0.set_xlabel(r'Power ($kW$)')
    ax0.legend()












.. _numpy: https://docs.scipy.org/doc/numpy-dev/user/index.html
.. _matplotlib.pyplot: https://matplotlib.org/index.html
.. _os: https://docs.python.org/3/library/os.html#module-os
.. _sys: https://docs.python.org/3/library/sys.html
.. _git: http://git-scm.com/
.. _downloaded: https://github.com/yabata/prodyn/archive/master.zip
