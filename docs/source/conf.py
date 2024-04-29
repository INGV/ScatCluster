import os
import sys

import sphinx_material
from pkg_resources import DistributionNotFound, get_distribution

# Fanciness to get version number
try:
    __version__ = get_distribution('scatcluster').version
except DistributionNotFound:
    __version__ = 'dev'

# Path setup
sys.path.insert(0, os.path.abspath('../../'))

# Project information
project = 'scatcluster'
author = 'Christopher Zerafa and Carlo Giunchi'
copyright = '2024, ' + author

version = __version__
release = __version__

# General configuration
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '**.ipynb_checkpoints',
]

extensions = [
    'sphinx.ext.duration', 'sphinx.ext.doctest', 'sphinx.ext.autodoc', 'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode', 'sphinx_gallery.load_style',
    'sphinx_favicon', 'sphinx_design', 'autoapi.extension', 'nbsphinx', 'numpydoc',
    'IPython.sphinxext.ipython_console_highlighting', 'sphinx_copybutton', 'nbsphinx', 'rtds_action'
]

favicons = [
    'scatcluster_no_text.png',
]

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
html_logo = '_static/scatcluster_no_text.png'

# Language
language = 'en'

nbsphinx_allow_errors = True

# # The name of your GitHub repository
rtds_action_github_token = os.environ['GITHUB_TOKEN']
rtds_action_github_repo = 'INGV/ScatCluster'
# # A GitHub personal access token is required, more info below
# # Whether or not to raise an error on Read the Docs if the
# # artifact containing the notebooks can't be downloaded (optional)
rtds_action_error_if_missing = False

# extensions.append('sphinx_material')
# html_theme_path = sphinx_material.html_theme_path()
# html_context = sphinx_material.get_html_context()
# html_theme = 'sphinx_material'
# html_title = 'ScatCluster'
# html_short_title = 'ScatCluster'
# html_theme_options = {
#     'nav_title': 'scatcluster',
#     'logo_icon': '&#xe869',
#     'color_primary': 'blue',
#     'color_accent': 'light-blue',
#     'repo_url': 'https://github.com/INGV/ScatCluster',
#     'repo_name': 'scatcluster',
#     'globaltoc_depth': 1,
#     'globaltoc_collapse': False,
#     'globaltoc_includehidden': False,
#     'nav_links': [],
# }
# # HTML theme
# html_show_sourcelink = False
# html_sidebars = {
#     '**': [
#         'logo-text.html',
#         'globaltoc.html',
#         'localtoc.html',
#         'searchbox.html',
#     ]
# }
