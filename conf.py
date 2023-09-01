# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'EPICS How-Tos'
copyright = '2019, EPICS Controls.'
author = 'EPICS'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "hoverxref.extension",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.graphviz",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_reredirects",
]

myst_enable_extensions =[
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "tasklist",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

master_doc = 'index'

html_theme_options = {
    'logo_only': True,
}
html_logo = "images/EPICS_white_logo_v02.png"


# -- Redirections specifications ---------------------------------------------

# Specify redirections to https://docs.epics-controls.org/
# instead of having a whole dedicated sub-website, i.e. readthedocs How-Tos
# "project":  https://docs.epics-controls.org/projects/how-tos/en/latest/
# See https://documatt.gitlab.io/sphinx-reredirects/usage.html
redirects = {
    #"index":
    #    "", # not redirected

    "getting-started/installation":
        "https://docs.epics-controls.org/en/latest/getting-started/installation.html",

    "getting-started/linux-packages":
        "https://docs.epics-controls.org/en/latest/getting-started/linux-packages.html",

    "getting-started/creating-ioc":
        "https://docs.epics-controls.org/en/latest/getting-started/creating-ioc.html",

    "getting-started/installation-windows":
        "https://docs.epics-controls.org/en/latest/getting-started/installation-windows.html",

    "getting-started/installation-windows-msys2":
        "https://docs.epics-controls.org/en/latest/getting-started/installation-windows-msys2.html",

    "getting-started/installation-windows-plain":
        "https://docs.epics-controls.org/en/latest/getting-started/installation-windows-plain.html",

    "getting-started/installation-windows-env":
        "https://docs.epics-controls.org/en/latest/getting-started/installation-windows-env.html",

    "building-epics/how-to-port-epics-to-a-new-os-architecture":
        "https://docs.epics-controls.org/en/latest/build-system/how-to-port-epics-to-a-new-os-architecture.html",

    "building-epics/configuring-vxworks-6_x":
        "https://docs.epics-controls.org/en/latest/build-system/configuring-vxworks-6_x.html",

    "building-epics/vxworks6_tornado":
        "https://docs.epics-controls.org/en/latest/build-system/vxworks6_tornado.html",

    "building-epics/cross-compile-epics-and-a-ioc-to-an-old-x86-linux":
        "https://docs.epics-controls.org/en/latest/build-system/cross-compile-epics-and-a-ioc-to-an-old-x86-linux.html",

    "applications/common-database-patterns":
        "https://docs.epics-controls.org/en/latest/process-database/common-database-patterns.html",

    "collaboration/how-to-run-an-epics-collaboration-meeting":
        "https://docs.epics-controls.org/en/latest/community/how-to-run-an-epics-collaboration-meeting.html",

    "collaboration/run-collaboration-meeting/organization":
        "https://docs.epics-controls.org/en/latest/community/run-collaboration-meeting/organization.html",

    "collaboration/run-collaboration-meeting/communications":
        "https://docs.epics-controls.org/en/latest/community/run-collaboration-meeting/communications.html",

    "collaboration/run-collaboration-meeting/facilities":
        "https://docs.epics-controls.org/en/latest/community/run-collaboration-meeting/facilities.html",

    "collaboration/run-collaboration-meeting/agenda":
        "https://docs.epics-controls.org/en/latest/community/run-collaboration-meeting/agenda.html",

    "writing-drivers/how-to-avoid-copying-arrays-with-waveformrecord":
        "https://docs.epics-controls.org/en/latest/process-database/how-to-avoid-copying-arrays-with-waveformrecord.html",

    "infrastructure-and-other/how-to-find-which-ioc-provides-a-pv":
        "https://docs.epics-controls.org/en/latest/process-database/how-to-find-which-ioc-provides-a-pv.html",
}
