# Configuration file for the Sphinx documentation builder.
# -- Path setup --------------------------------------------------------------
import os
import sys
from pathlib import Path
from typing import Any, Dict

import pydata_sphinx_theme
from sphinx.application import Sphinx

sys.path.append(str(Path(".").resolve()))
# -- Project information

path_str = str(Path(__file__).parent.parent)
print(path_str)


project = 'tutorial-dqrobotics-with-coppeliasim'
copyright = '2023, Juan Jose Quiroz Omana'
author = 'Juan Jose Quiroz Omana'

release = '0.1'
version = '0.1.0'

# -- General configuration

"""
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'hoverxref.extension', # https://sphinx-hoverxref.readthedocs.io/en/latest/index.html
    'sphinx_copybutton', # https://sphinx-copybutton.readthedocs.io/en/latest/
    'sphinx_design', # https://sphinx-design.readthedocs.io/en/latest/get_started.html
    'sphinx_favicon',
]
"""
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxext.rediraffe",
    "sphinx_design",
    "sphinx_copybutton",
    #"autoapi.extension",
    #"_extension.gallery_directive",
    # For extension examples and demos
    #"ablog",
    #"jupyter_sphinx",
    #"matplotlib.sphinxext.plot_directive",
    #"myst_nb",
    "sphinxcontrib.youtube",
    # "nbsphinx",  # Uncomment and comment-out MyST-NB for local testing purposes.
    "numpydoc",
    "sphinx_togglebutton",
    #"jupyterlite_sphinx",
    "sphinx_favicon",
]




intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for hoverxref.extension https://sphinx-hoverxref.readthedocs.io/en/latest/configuration.html
hoverxref_auto_ref = True

# -- Options for HTML output

html_theme = "pydata_sphinx_theme" #'sphinx_rtd_theme'
html_logo = path_str + "/build/html/_images/logo.svg"
html_favicon = path_str + "/build/html/_images/logo.svg"
html_theme_options = {

    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "navbar_align": "left"

}


# Define the json_url for our version switcher.
json_url = "https://pydata-sphinx-theme.readthedocs.io/en/latest/_static/switcher.json"

# Define the version we use for matching in the version switcher.
version_match = os.environ.get("READTHEDOCS_VERSION")
# If READTHEDOCS_VERSION doesn't exist, we're not on RTD
# If it is an integer, we're in a PR build and the version isn't correct.
if not version_match or version_match.isdigit():
    # For local development, infer the version to match from the package.
    release = pydata_sphinx_theme.__version__
    if "dev" in release or "rc" in release:
        version_match = "latest"
        # We want to keep the relative reference if we are in dev mode
        # but we want the whole url if we are effectively in a released version
        json_url = "_static/switcher.json"
    else:
        version_match = "v" + release

html_theme_options = {
    "external_links": [
        {
            "url": "https://dqrobotics.github.io/",
            "name": "DQ Robotics",
        },
        {
            "url": "https://numfocus.org/",
            "name": "NumFocus",
        },
        {
            "url": "https://numfocus.org/donate",
            "name": "Donate to NumFocus",
        },
    ],
    "header_links_before_dropdown": 4,
    "icon_links": [

        {
            "name": "GitHub",
            "url": "https://dqrobotics.github.io/",
            "icon": "fa-brands fa-github",
        },

        {
            "name": "DQ Robotics",
            "url": "https://dqrobotics.github.io/",
            "icon": path_str + "/build/html/_images/dqrobotics_logo_infinity2.svg",
            "type": "local",
            "attributes": {"target": "_blank"},
        },
    ],
    # alternative way to set twitter and github header icons
    # "github_url": "https://github.com/pydata/pydata-sphinx-theme",
    # "twitter_url": "https://twitter.com/PyData",
    "logo": {
        "text": "Home",
        "image_dark": "/docs/build/html/_images/logo.svg",
        "alt_text": "Tutorial: DQ Robotics with CoppeliaSim",
    },
    "use_edit_page_button": False,
    "show_toc_level": 1,
    "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    #"navbar_center": ["version-switcher", "navbar-nav"],
    #"announcement": "https://raw.githubusercontent.com/pydata/pydata-sphinx-theme/main/docs/_templates/custom-template.html",
    # "show_nav_level": 2,
    # "navbar_start": ["navbar-logo"],
    # "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    # "primary_sidebar_end": ["custom-template.html", "sidebar-ethical-ads.html"],
    # "article_footer_items": ["test.html", "test.html"],
    # "content_footer_items": ["test.html", "test.html"],
    # "footer_start": ["test.html", "test.html"],
    # "secondary_sidebar_items": ["page-toc.html"],  # Remove the source buttons
    "switcher": {
        "json_url": json_url,
        "version_match": version_match,
    },
    # "search_bar_position": "navbar",  # TODO: Deprecated - remove in future version
}

#html_sidebars = {
#    "**": ["about.html", "installation.html"]
#}

# -- Options for EPUB output
epub_show_urls = 'footnote'
