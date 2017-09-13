.. currentmodule:: mplstyle

.. _instal:

How to Install
========================
There are three ways of **mplstyle** installation. All of them are described below properly. 

Automatically
"""""""""""""""""""""""
Open Command Promt (cmd) , paste the line written in the following and push enter. **mplstyle** package will be added to Python search path automatically. 

::

    pip install git+https://github.com/tzipperle/mplstyle.git@master

Manually
"""""""""""""""""""""""
Follow the instruction written in the subsection `useful settings`_.

Locally
"""""""""""""""""""""""
::

    sys.path.append('C:/.../mplstyle/')

This command allows to use **mplstyle** for the case, when the package wasn't added to Python search path. Written in the brackets part ``'C:/.../mplstyle/'`` is the path to the directory, where **mplstyle** is located. This step is really necessary, if, for example, you have just `downloaded`_ or cloned (with `git`_) this repository to a directory of your choice, and you want to run examples' codes **inside** or **outside** this directory trying to figure out how **mplstyle** is working.

