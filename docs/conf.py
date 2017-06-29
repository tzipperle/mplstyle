# -*- coding: utf-8 -*-

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
]
#'sphinxcontrib.matlab',


#templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'mpl-style'
copyright = u'2017, Thomas Zipperle and Dennis Atabay'
author = u'Thomas Zipperle and Dennis Atabay'
version = '0.1'
release = '0.1'

exclude_patterns = ['_build']
#pygments_style = 'sphinx'

# HTML output

htmlhelp_basename = 'mpl-styledoc'

# LaTeX output

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'mpl-style.tex', u'mpl-style Documentation',
   u'Thomas Zipperl and Dennis Atabay', 'manual'),
]

# Manual page output

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'mpl-style', u'mpl-style Documentation',
     [author], 1)
]


# Texinfo output

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'mpl-style', u'mpl-style Documentation',
   author, 'mpl-style', 'Name Name',
   'Miscellaneous'),
]
# Epub output

# Bibliographic Dublin Core info.
epub_title = u'mpl-style'
epub_author = u'Thomas Zipperle and Dennis Atabay'
epub_publisher = u'Thomas Zipperle and Dennis Atabay'
epub_copyright = u'2017, Thomas Zipperle and Dennis Atabay'

epub_exclude_files = ['search.html']


# Intersphinx

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'http://docs.python.org/': None,
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/', None),
    'matplotlib': ('http://matplotlib.org/', None)}

