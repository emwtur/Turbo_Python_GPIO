from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

import sys

# Define required packages.
requires = []
# Assume spidev is required on non-windows & non-mac platforms (i.e. linux).
if sys.platform != 'win32' and sys.platform != 'darwin':
    requires.append('spidev')

setup(name              = 'TURBO_GPIO',
      version           = '0.1.3',
      author            = 'Per-Eric Larsson',
      author_email      = 'per-eric.larsson@densomlever.se',
      description       = '.',
      license           = 'MIT',
      url               = 'https://github.com/emwtur/Turbo_Python_GPIO/',
      install_requires  = requires,
      test_suite        = 'tests',
      packages          = find_packages())
