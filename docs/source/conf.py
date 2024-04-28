import os
import sys

# Path setup
sys.path.insert(0, os.path.abspath('../../'))

# Project information
project = 'scatcluster'
copyright = '2024, Christopher Zerafa and Carlo Giunchi'
author = 'Christopher Zerafa and Carlo Giunchi'

release = '0.0.1'
version = '0.0.1'

# General configuration
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '**.ipynb_checkpoints',
]

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_gallery.load_style',
    'sphinx_favicon',
    'sphinx_design',
    'autoapi.extension',
    'nbsphinx',
    'numpydoc',
    'IPython.sphinxext.ipython_console_highlighting',
]

# favicons = [
#     "logo_scatseisnet_notext.png",
# ]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = [
    'std',
]

templates_path = [
    '_templates',
]

# Options for HTML output

html_theme = 'pydata_sphinx_theme'

html_static_path = [
    '_static',
]

html_theme_options = {
    'pygment_light_style':
    'tango',
    'pygment_dark_style':
    'monokai',
    'github_url':
    'https://github.com/INGV/ScatCluster',
    'announcement':
    'This is a beta release of the scatcluster package. Please report any issues you find <a href=https://github.com/INGV/ScatCluster/issues>in the GitHub repository</a>.',
}

html_context = {
    'github_repo': 'https://github.com/INGV/ScatCluster',
}

# Options for AutoAPI
autoapi_type = 'python'
autoapi_dirs = ['../../src/scatcluster']
autosummary_generate = True

# Theme options are theme-specific and customize the look and feel of a theme
# further. For a list of options available for each theme, see the
# documentation.
# html_logo = "_static/logo_scatseisnet_notext.png"

# Language
language = 'en'

nbsphinx_allow_errors = True
