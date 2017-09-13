.. currentmodule:: mplstyle

.. _instal:

How to Install
========================
There are two ways of **mplstyle** installation. All of them are described below properly. 

From Source
"""""""""""""""""""""""
Open Command Promt (cmd) , paste the line written in the following and push enter. **mplstyle** package will be added to Python search path automatically. 

::

    pip install git+https://github.com/tzipperle/mplstyle.git@master


From Python
"""""""""""""""""""""""
Put the following command at the beginning of your code. 
::

    sys.path.append('C:/.../mplstyle/')

It allows to use **mplstyle** for the case, when the package wasn't added to Python search path. Written in the brackets part ``'C:/.../mplstyle/'`` is the path to the directory, where **mplstyle** is located. This step is really necessary, if, for example, you have just `downloaded`_ or cloned (with `git`_) this repository to a directory of your choice, and you want to run examples' codes **inside** or **outside** this directory trying to figure out how **mplstyle** is working.


.. _git: http://git-scm.com/
.. _downloaded: https://github.com/tzipperle/mplstyle/archive/master.zip



