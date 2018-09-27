# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    print('Python2 detected, trying workaround')
    from distutils.core import setup, find_packages

from eclipsecon import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), 'r').read()


if not __version__ or __version__ == '<VERSION>':
    raise RuntimeError("Package version not set!")

requirements = [
    "click",
    "google-api-python-client",
    "google-auth",
    "google-auth-oauthlib",
    "google-auth-httplib2"
]

setup(name="eclipsecon",
      author="Aljosha Friemann",
      author_email="a.friemann@automate.wtf",
      description="",
      keywords=[],
      version=__version__,
      license=read('LICENSE'),
      long_description=read('README.rst'),
      install_requires=requirements,
      classifiers=[],
      packages=find_packages(exclude=('tests', 'assets')),
      entry_points={ 'console_scripts': ['ec=eclipsecon.cli:root'] },
      include_package_data=True,
      package_data={'': ['assets/*']},
      platforms='linux')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
