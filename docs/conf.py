# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ORBE.AI'
copyright = '2021, Orbe.AI'
author = 'Orbe.AI'

release = '1.0'
version = '1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.images'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_logo = 'images/logo/logo_orbe.png'

html_theme_options = {
    'logo_only': True,
    'display_version': False
}

html_context = {
"display_github": False, # Add 'Edit on Github' link instead of 'View page source'
"last_updated": True,
"commit": False,
}

html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]


# -- Options for EPUB output
epub_show_urls = 'footnote'
