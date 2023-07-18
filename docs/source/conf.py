# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'tutorial-dqrobotics-with-coppeliasim'
copyright = '2023, Juan Jose Quiroz Omana'
author = 'Juan Jose Quiroz Omana'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'hoverxref.extension', # https://sphinx-hoverxref.readthedocs.io/en/latest/index.html
    'sphinx_copybutton', # https://sphinx-copybutton.readthedocs.io/en/latest/
    'sphinx_design' # https://sphinx-design.readthedocs.io/en/latest/get_started.html
]




intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
