


import os
import sys
from pathlib import Path
import datetime


sys.path.append(str(Path(".").resolve()))

sys.path.insert(0, os.path.abspath("."))
path_str = str(Path(__file__).parent.parent)

# -- Project information

project = 'tutorial-dqrobotics-with-coppeliasim'
copyright = str(datetime.date.today().year)+' Juan Jose Quiroz Omana'
author = 'Juan Jose Quiroz Omana'

release = '0.1'
version = '0.1.0'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_rtd_theme'
html_theme = "pydata_sphinx_theme"

html_static_path = ['_static']


html_logo = "./_static/basics/logo.svg"
html_favicon = "./_static/basics/logo.svg"


language = "en"
html_sourcelink_suffix = ""

html_theme_options = {
    "external_links": [

        {
            "url": "https://github.com/dqrobotics/learning-dqrobotics-in-matlab",
            "name": "Learn DQ Robotics",
        },
        {
            "url": "https://hal.science/hal-01478225v1",
            "name": "Learn Dual Quaternion Algebra",
        },
        {
            "url": "https://ros2-tutorial.readthedocs.io/en/latest/",
            "name": "Learn ROS2",
        },
    ],
    "header_links_before_dropdown": 4,
    "icon_links": [

        {
            "name": "GitHub",
            "url": "https://github.com/juanjqo/tutorial-dqrobotics-with-coppeliasim",
            "icon": "fa-brands fa-github",
        },

        {
            "name": "DQ Robotics",
            "url": "https://dqrobotics.github.io/",
            "icon": "https://raw.githubusercontent.com/juanjqo/tutorial-dqrobotics-with-coppeliasim/main/docs/_static/basics/dqrobotics_logo_infinity2.svg",
            "type": "local",
            "attributes": {"target": "_blank"},
        },
    ],
    # alternative way to set twitter and github header icons
    # "github_url": "https://github.com/pydata/pydata-sphinx-theme",
    # "twitter_url": "https://twitter.com/PyData",
    "logo": {
        "text": "Home",
        "image_dark": "./_static/basics/logo.svg",
        "alt_text": "MyProject",
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
    #"primary_sidebar_end": ["custom-template.html", "sidebar-ethical-ads.html"],
    # "article_footer_items": ["test.html", "test.html"],
    # "content_footer_items": ["test.html", "test.html"],
    # "footer_start": ["test.html", "test.html"],
    # "secondary_sidebar_items": ["page-toc.html"],  # Remove the source buttons

    #"primary_sidebar_end": ["sidebar-ethical-ads"],
    # "search_bar_position": "navbar",  # TODO: Deprecated - remove in future version
}

html_sidebars = {
    "**": ["sidebar-nav-bs", "sidebar-ethical-ads"],
    "index": [],
}

# -- Options for EPUB output
epub_show_urls = 'footnote'