from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='mplstyle',
    version='v0.3',
    packages=['mplstyle'],
    url='https://github.com/tzipperle/mplstyle',
    license='GNU General Public License v3.0',
    author='Thomas Zipperle',
    author_email='',
    description='Automation of changing plot settings in matplotlib',
    install_requires=requirements
)
