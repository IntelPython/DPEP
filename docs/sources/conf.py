# *****************************************************************************
# Copyright (c) 2020-2023, Intel Corporation All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# *****************************************************************************

# coding: utf-8
# Configuration file for the Sphinx documentation builder.

import errno
import shutil
from pathlib import Path

# -- Project information -----------------------------------------------------

project = "Data Parallel Extensions for Python*"
copyright = "2020-2023, Intel Corporation"
author = "Intel Corporation"

# The full version, including alpha/beta/rc tags
release = "0.1"

# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.programoutput",
    "sphinxcontrib.googleanalytics",
    "nbsphinx",
    "IPython.sphinxext.ipython_console_highlighting",
]

googleanalytics_id = "G-KVSVYMBQ0W"
googleanalytics_enabled = True

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']
templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sdc-sphinx-theme"

html_theme_path = ["."]

html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

html_sidebars = {
    "**": ["globaltoc.html", "sourcelink.html", "searchbox.html", "relations.html"],
}

html_show_sourcelink = False

# -- Todo extension configuration  ----------------------------------------------
todo_include_todos = True
todo_link_only = True

intersphinx_mapping = {}

# -- Prepend module name to an object name or not -----------------------------------
add_module_names = False

# -- Copy notebooks into ./docs/sources/notebooks -----------------------------------
notebooks_src_path = "../../notebooks"
notebooks_dst_path = "notebooks"

dirpath = Path(notebooks_dst_path)
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)

try:
    shutil.copytree(notebooks_src_path, notebooks_dst_path)
except OSError as exc:  # python >2.5
    if exc.errno in (errno.ENOTDIR, errno.EINVAL):
        shutil.copy(notebooks_src_path, notebooks_dst_path)
    else:
        raise
