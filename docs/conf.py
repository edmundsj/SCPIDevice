# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../source/'))
sys.path.insert(0, os.path.abspath('../test/'))

# These two don't currently work - I need to figure out how to change my conda environment
#import pockels_modulator.simulations.meep_AlN_reflectance_spectra
#import pockels_modulator.simulations.meep_mirror_reflectance_spectra
#import pockels_modulator.simulations.rcwa_bragg_mirror

#from pockels_modulator.processing_code.XRD import generate_figures
#from pockels_modulator.processing_code.raman import generate_figures
#from pockels_modulator.processing_code.iv_curves import BRK1
#from pockels_modulator.processing_code.LCR import ALN5_6, IMP1
#from pockels_modulator.processing_code.photocurrent import BRAGG1, REFL1

#generate_transfer_functions, \
#generate_xrd_figures, \
#generate_xrd_figures, \
#generate_raman_figures, \
#generate_blackbody_figure, \
#generate_electronics_figures, \
#generate_fft_figures, \
#generate_meep_predictions, \
#generate_cv_curves, \
#generate_lcr_curves, \
#generate_adc_figures, \
#generate_bragg_figures, \

# -- Project information -----------------------------------------------------

project = 'Jordan Edmunds\' Ph.D.'
copyright = '2020, Jordan Edmunds'
author = 'Jordan Edmunds'
master_doc = 'index'
numfig = True


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        'sphinx_rtd_theme',
        'sphinx.ext.autodoc',
        'sphinx.ext.coverage',
        'sphinx.ext.napoleon',
        'sphinx.ext.mathjax',
        'sphinxcontrib.bibtex',
]
#autosummary_generate = True

bibtex_bibfiles = ['refs.bib']
bibtex_default_style = 'unsrt'


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'pockels_modulator/designs/canceler_simple/*']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
