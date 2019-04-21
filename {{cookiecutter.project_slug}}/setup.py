#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='{{cookiecutter.project_slug}}',
    version='0.1.0',
    license='Apache License, Version 2.0',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    url='https://github.com/dbradf/{{cookiecutter.project_slug}}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=[
        'Click==7.0',
        'PyYAML==5.1',
        'requests==2.21.0',
    ],
    entry_points='''
        [console_scripts]
        cli={{cookiecutter.project_slug}}.cli.main:main
    ''',
)
