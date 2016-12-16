# Python-Tools

Keep them in a separate directory that [keep always on the Python search path](http://stackoverflow.com/q/17806673/2375855) so you can include them like installed site-packages.

## Installation(ish)

I just clone this repo into the directory that is returned by the following Python snippet:

    import os, site
    from sys import version_info as ver
    print(os.path.join(site.USER_BASE, 
                       'Python{}{}'.format(ver.major, ver.minor), 
                       'site-packages'))

Depending on your operating system and Python version, this evaluates to

    Windows, Python 3.5: C:\Users\*Name*\AppData\Roaming\Python\Python35\site-packages


## matplotlib_settings

Set own plot and color style. TODO: ***

### Dependencies
  - [matplotlib](http://http://matplotlib.org/)
