#!/usr/bin/env python
"""
obs
===

:copyright: (c) 2015 Functional Software, Inc
:license: Apache 2.0, see LICENSE for more details.
"""
from __future__ import absolute_import, unicode_literals

import os.path

from setuptools import setup, find_packages


# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
for m in ('multiprocessing', 'billiard'):
    try:
        __import__(m)
    except ImportError:
        pass

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))

tests_require = [
    'flake8>=2.1.0,<2.2.0',
    'mock>=1.0.1,<1.1.0',
    'pytest>=2.5.0,<2.6.0',
    'pytest-cov>=1.6,<1.7',
    'pytest-timeout>=0.3,<0.4',
    'pytest-xdist>=1.9,<1.10',
]


install_requires = [
]

setup(
    name='obs',
    version='0.0.0',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='https://github.com/getsentry/obs',
    description='',
    long_description=open('README.md').read(),
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'test': tests_require,
    },
    license='Apache 2.0',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
