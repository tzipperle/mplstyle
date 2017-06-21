# mpl-style
Short description.  **TODO**

[![Documentation Status](https://readthedocs.org/projects/mpl-style/badge/?version=latest)](http://mpl-style.readthedocs.io/en/latest/?badge=latest)

## Features

Set own plot and color style. **TODO**

## Dependencies
  - [matplotlib](http://http://matplotlib.org/)
  - [cycler](http://matplotlib.org/cycler/)
  - [numpy](http://www.numpy.org/)

**check if there are more**

## Useful settings: Custom directory for own packages

Add the package `mpl-style` automatically to sys.path:

  1. Create a directory anywhere, e.g. `C:\Users\Name\Documents\Python\Libs`.
  2. Add the file `sitecustomize.py` to the site-packages folder of the Python installation, i.e. in `C:\Anaconda3\Lib\site-packages` (for all users) or site.USER_SITE (for a single user).
  3. This file then is filled with the following code:

      ```
      import site
      site.addsitedir(r'C:\Users\ojdo\Any\Folder\You\Like\Libs')
      ```

  4. The directory now is automatically added to sys.path in every (I)Python session.

Package site, that is automatically imported during every start of Python, also tries to import the package sitecustomize for custom package path modifications.

Source: [Stack Overflow](http://stackoverflow.com/q/17806673/2375855)