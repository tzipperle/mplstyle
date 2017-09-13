.. currentmodule:: mplstyle

.. _instal:

How to Install
========================



first
"""""""""""""""""""""""

There are three ways of 
::

    sys.path.append('C:/.../mplstyle/')

This command allows to use **mplstyle** for the case, when the package wasn't added to Python search path. Written in the brackets part ``'C:/.../mplstyle/'`` is the path to the directory, where **mplstyle** is located. This step is really necessary, if, for example, you have just `downloaded`_ or cloned (with `git`_) this repository to a directory of your choice, and you want to run examples' codes **inside** or **outside** this directory trying to figure out how **mplstyle** is working.

.. note::


        There are two ways of adding **mplstyle** package to the sys.path, which will allow to include it as installed site-package. This procedure can be done automatically by running ``setup.py`` file or manually according to the instruction written in the subsection `useful settings`_.